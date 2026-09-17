#!/usr/bin/env python3
"""Steward's local Apple Calendar/Reminders connector. JSON stdin -> JSON stdout.

Operations: status, connect, containers, list, get, create, update, delete,
create-container, rename-container, delete-container (empty only).
Container creation takes source and name; renaming takes calendar and name.
app: calendar|reminders|notes. calendar: discovered container ID.
Calendar list requires start/end ISO8601 timestamps (maximum 93 days).
Reminders list optionally includes includeCompleted:true.
Create requires token (stable UUID for retry recovery), fields.title, and for events
fields.start/end. Update/delete require id. Mutations preview unless --apply.
Fields: calendar title/start/end/notes/location/allDay; reminders
title/notes/due/completed/priority/remindAt. Calendar alertMinutesBefore sets
a notification alarm; null clears alarms. Reminder remindAt uses an explicit
timestamp; null clears alarms. Notes title/text/appendText; replacement text
requires expectedModified from get. due:null clears a due date. Dates need offsets.
Run --build to compile locally (macOS 14+, Apple developer tools required).
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import fcntl
import subprocess
import sys
import tempfile
from datetime import datetime

HERE = Path(__file__).resolve().parent
CACHE = Path.home() / 'Library/Caches/Steward/apple'
WRITES = {'create', 'update', 'delete', 'create-container', 'rename-container', 'delete-container'}


def timestamp(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})', value):
        raise ValueError('Date must be a string with an explicit UTC offset')
    d = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if d.tzinfo is None or d.microsecond:
        raise ValueError('Use ISO8601 seconds and explicit UTC offset')
    return d


def validate(r):
    if not isinstance(r, dict):
        raise ValueError('Expected JSON object')
    op = r.get('op')
    if op not in {'status', 'connect', 'containers', 'list', 'get', *WRITES}:
        raise ValueError('Unknown op')
    allowed = {'op', 'app', 'calendar', 'id', 'fields', 'token', 'start', 'end', 'includeCompleted', 'source', 'name', 'expectedModified'}
    if set(r) - allowed:
        raise ValueError('Unknown request keys: ' + ', '.join(sorted(set(r) - allowed)))
    if op == 'status':
        return r
    app = r.get('app')
    if app not in {'calendar', 'reminders', 'notes'}:
        raise ValueError('app must be calendar, reminders or notes')
    if op not in {'connect', 'containers', 'create-container'} and not isinstance(r.get('calendar'), str):
        raise ValueError('Choose a container by its discovered calendar ID')
    if op in {'get', 'update', 'delete'} and not r.get('id'):
        raise ValueError('id is required')
    if op == 'list' and app == 'calendar':
        start, end = timestamp(r.get('start')), timestamp(r.get('end'))
        if not 0 < (end - start).total_seconds() <= 93 * 86400:
            raise ValueError('Calendar query must cover 1 second to 93 days')
    if op in {'create-container', 'rename-container'}:
        if not isinstance(r.get('name'), str) or not r['name'].strip(): raise ValueError('Container name is required')
    if op == 'create-container' and not isinstance(r.get('source'), str): raise ValueError('Discovered source ID is required')
    f = r.get('fields', {})
    if not isinstance(f, dict):
        raise ValueError('fields must be an object')
    fields = {'title', 'notes', 'location', 'start', 'end', 'allDay', 'alertMinutesBefore'} if app == 'calendar' else ({'title', 'notes', 'due', 'completed', 'priority', 'remindAt'} if app == 'reminders' else {'title', 'text', 'appendText'})
    if set(f) - fields:
        raise ValueError('Unsupported fields: ' + ', '.join(sorted(set(f) - fields)))
    for k, v in f.items():
        if k in {'allDay', 'completed'}:
            if type(v) is not bool: raise ValueError(k + ' must be boolean')
        elif k == 'alertMinutesBefore':
            if v is not None and (type(v) is not int or not 0 <= v <= 40320): raise ValueError('alertMinutesBefore must be null or 0...40320')
        elif k == 'priority':
            if type(v) is not int or not 0 <= v <= 9: raise ValueError('priority must be 0...9')
        elif k in {'due', 'remindAt'} and v is None:
            pass
        elif not isinstance(v, str):
            raise ValueError(k + ' must be a string')
        if k in {'start', 'end', 'due', 'remindAt'} and v is not None:
            timestamp(v)
    if 'text' in f and 'appendText' in f: raise ValueError('Choose replacement text or appendText')
    if op == 'update' and app == 'notes' and not r.get('expectedModified'):
        raise ValueError('Read note first and supply expectedModified for any update')
    if op == 'create':
        if app == 'notes' and 'appendText' in f: raise ValueError('Use text for initial note content')
        import uuid
        if not isinstance(r.get('token'), str): raise ValueError('token must be a UUID string')
        uuid.UUID(r['token'])
        if not f.get('title', '').strip(): raise ValueError('title is required')
        if app == 'calendar' and not {'start', 'end'} <= set(f):
            raise ValueError('Calendar create requires start and end')
    if 'start' in f and 'end' in f and timestamp(f['end']) <= timestamp(f['start']):
        raise ValueError('end must follow start')
    if f.get('allDay'):
        for key in ('start', 'end'):
            if key in f and any((timestamp(f[key]).hour, timestamp(f[key]).minute, timestamp(f[key]).second)):
                raise ValueError('All-day boundaries must be local midnight, with exclusive end')
    if 'title' in f and not f['title'].strip(): raise ValueError('title cannot be blank')
    return r


def build():
    if platform.system() != 'Darwin': raise ValueError('This connector requires macOS')
    digest = hashlib.sha256((HERE / 'apple.swift').read_bytes() + (HERE / 'Info.plist').read_bytes()).hexdigest()
    binary = CACHE / 'steward-apple'
    stamp = CACHE / 'build.sha256'
    if binary.exists() and stamp.exists() and stamp.read_text() == digest:
        return binary
    CACHE.mkdir(parents=True, exist_ok=True)
    temp = CACHE / ('build-' + str(os.getpid()))
    compilers = [Path('/Library/Developer/CommandLineTools/usr/bin/swiftc'), Path('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc')]
    errors = []
    for compiler in compilers:
        if not compiler.exists(): continue
        cmd = [str(compiler), '-target', platform.machine() + '-apple-macosx14.0', str(HERE / 'apple.swift'), '-o', str(temp), '-Xlinker', '-sectcreate', '-Xlinker', '__TEXT', '-Xlinker', '__info_plist', '-Xlinker', str(HERE / 'Info.plist')]
        sdk = Path('/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk') if str(compiler).startswith('/Applications/') else Path('/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk')
        if sdk.exists(): cmd += ['-sdk', str(sdk)]
        cmd += ['-module-cache-path', str(CACHE / 'modules')]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if result.returncode == 0:
            temp.replace(binary); stamp.write_text(digest); return binary
        errors.append(result.stderr[-3000:])
    raise ValueError('Could not compile. Install/repair Apple Command Line Tools.\n' + '\n'.join(errors))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--apply', action='store_true', help='Execute the authorized mutation; default returns a local preview')
    p.add_argument('--build', action='store_true', help='Compile without requesting app access')
    a = p.parse_args()
    try:
        if a.build:
            print(json.dumps({'binary': str(build())})); return 0
        r = validate(json.load(sys.stdin))
        if r['op'] in WRITES and not a.apply:
            print(json.dumps({'state': 'preview', 'request': r})); return 0
        r['apply'] = a.apply
        CACHE.mkdir(parents=True, exist_ok=True)
        native_script = r.get('app') == 'notes'
        binary = None if native_script else build()
        with (CACHE / 'operation.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            if native_script:
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json') as request_file:
                    json.dump(r, request_file); request_file.flush()
                    result = subprocess.run(['/usr/bin/osascript', '-l', 'JavaScript', str(HERE / 'notes.js'), request_file.name], text=True, capture_output=True, timeout=100)
            else:
                result = subprocess.run([str(binary)], input=json.dumps(r), text=True, capture_output=True, timeout=100)
        if result.stdout: print(result.stdout.strip())
        if result.stderr: print(result.stderr.strip(), file=sys.stderr)
        if result.returncode: return result.returncode
        payload = json.loads(result.stdout)
        if r['op'] == 'create-container' and r.get('app') == 'notes' and payload.get('state') == 'created':
            c = payload['container']
            if not c['shared']:
                policy_path = Path.home() / 'Library/Application Support/Steward/apple-policy.json'
                policy = json.loads(policy_path.read_text())
                policy.setdefault('notes', {})[c['id']] = {'name': c['name'], 'write': True, 'provenance': 'created-private-by-Steward'}
                temp = policy_path.with_suffix('.tmp')
                temp.write_text(json.dumps(policy, indent=2)); temp.chmod(0o600); temp.replace(policy_path)
        return 1 if 'error' in payload else 0
    except (ValueError, OSError, subprocess.SubprocessError) as e:
        print(json.dumps({'error': str(e), 'state': 'failed-or-uncertain', 'recovery': 'Read back the destination before retrying a mutation; do not use a new create token.'}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
