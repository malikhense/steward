#!/usr/bin/env python3
"""Steward's resumable connection choices and observed access, stored in personal memory.

Select/skip apps only from the user's choices. probe verifies actual connector reads;
record-ui records a completed host app-control observation, not an app installation.
Writes preview unless --apply. Disconnect stops Steward context use; it does not
revoke macOS permissions. Registry data never grants external action authorization.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

APPS = {
    'calendar': ('Calendar', 'Availability, commitments, and realistic time estimates', 'connector'),
    'reminders': ('Reminders', 'Open tasks and observed completion', 'connector'),
    'notes': ('Notes', 'Plans and reference material in selected folders', 'connector'),
    'contacts': ('Contacts', 'Correct people and contact details', 'app-control'),
    'mail': ('Mail', 'Relevant commitments, decisions, and correspondence', 'app-control'),
    'messages': ('Messages', 'Relevant conversations and relationship context', 'app-control'),
    'finder': ('Finder', 'Documents in selected folders', 'filesystem'),
    'shortcuts': ('Shortcuts', 'Existing reusable actions; inspect before running', 'cli-app-control'),
}
SCHEMA = 1
APPLE = Path(__file__).resolve().parents[2] / 'steward-apple/scripts/apple.py'


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def registry_path(vault):
    p = Path(vault).expanduser().absolute()
    target = p / 'System/Connections.json'
    if any(x.is_symlink() for x in [target, *target.parents]):
        raise ValueError('Connection store must use an inspected non-symlink path')
    if not p.is_dir():
        raise ValueError('Resolve the existing memory folder first')
    return target


def read(path):
    if not path.exists():
        return {'schema': SCHEMA, 'apps': {}, 'updated': None}
    value = json.loads(path.read_text())
    if value.get('schema') != SCHEMA or not isinstance(value.get('apps'), dict):
        raise ValueError('Unknown connection registry; preserve and inspect it')
    return value


def save(path, value, previous):
    # Optimistic file check: never replace a changed registry silently.
    current = path.read_bytes() if path.exists() else None
    if current != previous:
        raise ValueError('Connection choices changed during this operation; reread and reconcile')
    path.parent.mkdir(parents=True, exist_ok=True)
    value['updated'] = now()
    with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, delete=False) as f:
        temporary = Path(f.name)
        json.dump(value, f, indent=2); f.write('\n')
    try:
        temporary.chmod(0o600)
        os.replace(temporary, path)
    finally:
        if temporary.exists(): temporary.unlink()


def status(value):
    rows = []
    for app, (name, purpose, route) in APPS.items():
        entry = value['apps'].get(app, {})
        rows.append({'app': app, 'name': name, 'purpose': purpose, 'route': route,
                     **entry, 'choice': entry.get('choice', 'not-offered'),
                     'access': entry.get('access', 'unverified')})
    pending = [r['app'] for r in rows if r['choice'] == 'selected' and r['access'] != 'verified']
    return {'apps': rows, 'pending': pending,
            'connectionsReviewed': all(r['choice'] != 'not-offered' for r in rows[:6]),
            'contextRule': 'Use selected, verified sources only within saved scope and the current task; refresh live facts.'}


def execute(args, value):
    apps = value['apps']
    if args.command in {'select', 'skip', 'disconnect'}:
        for app in args.apps:
            entry = apps.setdefault(app, {})
            if args.command == 'select':
                was_selected = entry.get('choice') == 'selected' and entry.get('scope') == args.scope
                entry.update(choice='selected', context=args.context, scope=args.scope, selectedAt=now())
                if not was_selected: entry.update(access='unverified', evidence=None, verifiedAt=None, containers=[], next=None)
            else:
                entry.update(choice='skipped' if args.command == 'skip' else 'disconnected', context=False,
                             access='unverified', evidence=None, verifiedAt=None, scope=None,
                             containers=[], next=None)
        return {'state': 'recorded', 'apps': args.apps}
    app = args.app
    entry = apps.get(app, {})
    if entry.get('choice') != 'selected':
        raise ValueError('App must be selected by the user before verification')
    if args.command == 'probe':
        if APPS[app][2] != 'connector':
            raise ValueError('Use actual host app control, then record-ui; installation alone is not verified access')
        try:
            result = subprocess.run([sys.executable, str(APPLE)], input=json.dumps({'op': 'connect', 'app': app}),
                                    text=True, capture_output=True, timeout=240)
        except (OSError, subprocess.SubprocessError) as error:
            entry.update(access='blocked', verifiedAt=None, evidence=None, containers=[], next=str(error))
            return {'state':'blocked', 'app':app, 'next':entry['next']}
        try:
            payload = json.loads(result.stdout)
        except ValueError:
            payload = {'error': result.stderr.strip() or 'Connector returned no readable result'}
        if result.returncode or 'containers' not in payload:
            entry.update(access='blocked', verifiedAt=None, evidence=None,
                         next=payload.get('error', 'Inspect connector access and retry'), containers=[])
            return {'state': 'blocked', 'app': app, 'next': entry['next']}
        # Container metadata only; never copy event, task, or note content into this register.
        entry.update(access='verified', verifiedAt=now(), route='connector',
                     evidence='Connector returned actual container discovery', next=None,
                     containers=payload['containers'])
        return {'state': 'verified', 'app': app, 'containers': len(payload['containers']), 'writes': 'not-established-by-this-read'}
    if args.command == 'record-ui':
        if not args.evidence.strip(): raise ValueError('Record a concrete observation')
        if args.access != 'verified' and not args.next: raise ValueError('Blocked/unavailable access needs a concrete next step')
        if APPS[app][2] == 'connector':
            raise ValueError('Use probe for Calendar, Reminders, or Notes')
        entry.update(access=args.access, route=APPS[app][2],
                     verifiedAt=now() if args.access == 'verified' else None,
                     evidence=args.evidence, next=args.next)
        return {'state': args.access, 'app': app, 'verification': 'host-observation-recorded'}
    raise ValueError('Unknown command')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--vault', help='Existing personal memory folder; required except catalog')
    p.add_argument('--apply', action='store_true', help='Save choices or perform actual verification; default previews')
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('catalog'); sub.add_parser('status')
    select = sub.add_parser('select')
    select.add_argument('--apps', nargs='+', choices=APPS, required=True)
    select.add_argument('--context', action=argparse.BooleanOptionalAction, default=True)
    select.add_argument('--scope', required=True, help='User-approved relevant context boundaries, accounts or folders')
    for command in ['skip', 'disconnect']:
        item = sub.add_parser(command); item.add_argument('--apps', nargs='+', choices=APPS, required=True)
    probe = sub.add_parser('probe'); probe.add_argument('--app', choices=APPS, required=True)
    record = sub.add_parser('record-ui'); record.add_argument('--app', choices=APPS, required=True)
    record.add_argument('--access', choices=['verified', 'blocked', 'unavailable'], required=True)
    record.add_argument('--evidence', required=True, help='Actual host observation; omit private content')
    record.add_argument('--next', help='Precise unresolved step')
    args = p.parse_args()
    try:
        if args.command == 'catalog':
            print(json.dumps(status({'apps': {}}))); return 0
        if not args.vault: raise ValueError('--vault is required; use a portable continuation note for no-storage trials')
        path = registry_path(args.vault)
        previous = path.read_bytes() if path.exists() else None
        value = read(path)
        if args.command == 'status':
            print(json.dumps(status(value))); return 0
        if not args.apply:
            print(json.dumps({'state': 'preview', 'operation': args.command, 'arguments': vars(args)})); return 0
        result = execute(args, value)
        save(path, value, previous)
        print(json.dumps(result)); return 0 if result['state'] not in {'blocked', 'unavailable'} else 2
    except (OSError, ValueError, subprocess.SubprocessError) as e:
        print(json.dumps({'error': str(e)})); return 1


if __name__ == '__main__':
    sys.exit(main())
