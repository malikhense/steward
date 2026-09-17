#!/usr/bin/env python3
"""Install or update Steward's complete skill suite with previews and local-edit protection."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = '.steward-installation.json'


def contents(folder):
    if folder.is_symlink(): raise ValueError('Symlink skill destination needs inspection: ' + str(folder))
    result = {}
    for path in folder.rglob('*'):
        if path.is_symlink(): raise ValueError('Symlink file needs inspection: ' + str(path))
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
            result[str(path.relative_to(folder))] = path.read_bytes()
    return result


def hashes(data):
    return {k: hashlib.sha256(v).hexdigest() for k, v in data.items()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dest', required=True, help='Actual host skill directory')
    p.add_argument('--apply', action='store_true', help='Install/update after preflight; default previews')
    p.add_argument('--update', action='store_true', help='Update previously managed, unmodified files; backs up changed folders')
    args = p.parse_args()
    dest = Path(args.dest).expanduser().absolute()
    try:
        if any(x.is_symlink() for x in [dest, *dest.parents]): raise ValueError('Resolve a non-symlink destination first')
        if dest.exists() and not dest.is_dir(): raise ValueError('Destination is not a directory')
        receipt_path = dest / RECEIPT
        if receipt_path.is_symlink(): raise ValueError('Receipt is a symlink; inspect it first')
        old = json.loads(receipt_path.read_text()) if receipt_path.exists() else {'skills': {}}
        if not isinstance(old.get('skills'), dict): raise ValueError('Invalid installation receipt')
        subprocess.run([sys.executable, str(ROOT / 'scripts/check.py')], check=True, capture_output=True, text=True)
        sources = sorted(p.parent for p in (ROOT / 'skills').glob('*/SKILL.md'))
        missing, matching, changed = [], [], []
        planned = {}
        for source in sources:
            target = dest / source.name
            data = contents(source); planned[source.name] = hashes(data)
            if not target.exists(): missing.append(source); continue
            if not target.is_dir(): raise ValueError('Skill target is not a directory: ' + source.name)
            actual = contents(target)
            if actual == data: matching.append(source.name); continue
            if not args.update or hashes(actual) != old['skills'].get(source.name):
                raise ValueError('Existing skill differs: ' + source.name + '. Local/unmanaged changes preserved; reconcile before updating.')
            changed.append(source)
        retiring = []
        for source in sources:
            if not source.name.startswith('steward-'): continue
            legacy = 'kernel-' + source.name[len('steward-'):]
            target = dest / legacy
            if not target.exists() and not target.is_symlink(): continue
            if not args.update or not target.is_dir() or hashes(contents(target)) != old['skills'].get(legacy):
                raise ValueError('Legacy skill has unmanaged/local changes: ' + legacy + '. Preserve and reconcile before migration.')
            retiring.append(legacy)
        backup = None
        if args.apply:
            dest.mkdir(parents=True, exist_ok=True)
            # Preserve recoverable originals before the first replacement.
            if changed or retiring:
                backups = dest / '.steward-backups'
                if backups.is_symlink(): raise ValueError('Backup destination is a symlink; inspect it first')
                backups.mkdir(exist_ok=True)
                stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
                backup = backups / (stamp + '.zip')
                with zipfile.ZipFile(backup, 'x', zipfile.ZIP_DEFLATED) as archive:
                    if receipt_path.exists(): archive.write(receipt_path, RECEIPT)
                    for name in [source.name for source in changed] + retiring:
                        for rel, data in contents(dest / name).items(): archive.writestr(name + '/' + rel, data)
            for source in missing + changed:
                target = dest / source.name
                # Stage the complete folder first. One installer writer at a time.
                with tempfile.TemporaryDirectory(dir=dest, prefix='.steward-stage-') as tmp:
                    staged = Path(tmp) / source.name
                    shutil.copytree(source, staged, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
                    if source in changed:
                        if hashes(contents(target)) != old['skills'].get(source.name): raise ValueError('Local edits appeared during update: '+source.name)
                        shutil.rmtree(target)
                    staged.replace(target)
            for source in sources:
                if hashes(contents(dest / source.name)) != planned[source.name]: raise ValueError('Read-back mismatch: ' + source.name)
            for legacy in retiring:
                if hashes(contents(dest / legacy)) != old['skills'].get(legacy):
                    raise ValueError('Local edits appeared during migration: ' + legacy)
            for legacy in retiring:
                shutil.rmtree(dest / legacy)
            receipt = {'schema': 1, 'version': (ROOT / 'VERSION').read_text().strip(), 'skills': planned}
            # An identical reinstall should not churn this record.
            with tempfile.NamedTemporaryFile(mode='w', dir=dest, prefix='.steward-receipt-', delete=False) as stream:
                temp = Path(stream.name)
                stream.write(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
            try:
                temp.replace(receipt_path)
            finally:
                if temp.exists(): temp.unlink()
        print(json.dumps({'applied': args.apply, 'version': (ROOT / 'VERSION').read_text().strip(),
                          'missing': [x.name for x in missing], 'already_matching': matching,
                          'updating': [x.name for x in changed], 'retiring': retiring, 'destination': str(dest),
                          'backup': str(backup) if backup else None, 'next': 'Use $steward to get started.'}))
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(str(error) + '\nNo conflicting file is intentionally overwritten. If copying began before an I/O failure, inspect partial results and the backup before retrying.', file=sys.stderr)
        return 1


if __name__ == '__main__': sys.exit(main())
