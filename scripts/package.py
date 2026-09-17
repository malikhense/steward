#!/usr/bin/env python3
"""Build a versioned Steward plugin archive from an explicit source allowlist."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile
ROOT = Path(__file__).resolve().parents[1]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', required=True, help='New output directory; existing files are preserved')
    args=p.parse_args()
    out=Path(args.out).expanduser().absolute()
    try:
        if any(x.is_symlink() for x in [out,*out.parents]):raise ValueError('Output must not use symlinks')
        version=(ROOT/'VERSION').read_text().strip()
        manifest=json.loads((ROOT/'packaging/plugin.json').read_text())
        if manifest['version'] != version:raise ValueError('Manifest and VERSION disagree')
        targets=[out/'steward',out/f'steward-{version}.zip',out/'SHA256SUMS']
        if any(x.exists() for x in targets):raise ValueError('Output already contains a package; choose a new output directory')
        subprocess.run([sys.executable,str(ROOT/'scripts/check.py')],check=True,capture_output=True,text=True)
        out.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=out,prefix='.build-') as temp:
            plugin=Path(temp)/'steward';plugin.mkdir()
            for name in ['skills','scripts','tests','docs','packaging','assets']:
                source=ROOT/name
                if any(x.is_symlink() for x in source.rglob('*')):raise ValueError('Unexpected source symlink: '+name)
                shutil.copytree(source,plugin/name,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
            for name in ['README.md','INSTALL.md','LICENSE','VERSION','AGENTS.md','CHANGELOG.md']:
                shutil.copy2(ROOT/name,plugin/name)
            (plugin/'.codex-plugin').mkdir()
            (plugin/'.codex-plugin/plugin.json').write_text(json.dumps(manifest,indent=2)+'\n')
            # Relative skill references must resolve from the shipped tree too.
            subprocess.run([sys.executable,str(plugin/'scripts/check.py')],check=True,capture_output=True,text=True)
            zip_path=Path(temp)/f'steward-{version}.zip'
            with zipfile.ZipFile(zip_path,'x',zipfile.ZIP_DEFLATED) as z:
                for path in sorted(plugin.rglob('*')):
                    if path.is_file():
                        info=zipfile.ZipInfo(str(path.relative_to(plugin.parent)),date_time=(2026,1,1,0,0,0))
                        info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
                        z.writestr(info,path.read_bytes())
            digest=hashlib.sha256(zip_path.read_bytes()).hexdigest()
            plugin.replace(targets[0]);zip_path.replace(targets[1])
            targets[2].write_text(digest+'  '+targets[1].name+'\n')
        print(json.dumps({'version':version,'plugin':str(targets[0]),'archive':str(targets[1]),'sha256':digest}));return 0
    except (OSError,ValueError,subprocess.CalledProcessError) as e:
        print(str(e),file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
