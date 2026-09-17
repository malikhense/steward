import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
import uuid

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/steward-apple/scripts/apple.py'
spec = importlib.util.spec_from_file_location('apple', SCRIPT)
apple = importlib.util.module_from_spec(spec)
spec.loader.exec_module(apple)

class AppleTests(unittest.TestCase):
    def event(self):
        return {'op':'create','app':'calendar','calendar':'fixture','token':str(uuid.uuid4()),'fields':{'title':'A "quoted" title; $(not-executed)','start':'2026-09-16T10:00:00-07:00','end':'2026-09-16T11:00:00-07:00'}}
    def test_preview_never_builds_or_opens_apps(self):
        r=self.event()
        p=subprocess.run([sys.executable,str(SCRIPT)],input=json.dumps(r),capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stdout)
        self.assertEqual(json.loads(p.stdout),{'state':'preview','request':r})
    def test_invalid_time_and_field_requests(self):
        cases=[]
        for start in ['2026-09-16T10:00:00','2026-09-16 10:00:00-07:00','tomorrow',None]:
            r=self.event();r['fields']['start']=start;cases.append(r)
        r=self.event();r['fields']['end']=r['fields']['start'];cases.append(r)
        r=self.event();r['fields']['attendees']=['someone'];cases.append(r)
        r=self.event();r['fields']['allDay']=True;cases.append(r)
        r=self.event();r['token']=None;cases.append(r)
        for r in cases:
            with self.subTest(r=r),self.assertRaises(ValueError): apple.validate(r)
    def test_mutations_require_exact_destination(self):
        for op in ['update','delete']:
            with self.assertRaises(ValueError):apple.validate({'op':op,'app':'reminders','calendar':'x'})
    def test_reminder_completion_and_due_clear(self):
        apple.validate({'op':'update','app':'reminders','calendar':'x','id':'y','fields':{'completed':True,'due':None}})
        with self.assertRaises(ValueError):apple.validate({'op':'update','app':'reminders','calendar':'x','id':'y','fields':{'completed':'true'}})
    def test_alarm_payloads_and_notes_conflict_guard(self):
        r=self.event();r['fields']['alertMinutesBefore']=15;apple.validate(r)
        r['fields']['alertMinutesBefore']=None;apple.validate(r)
        r['fields']['alertMinutesBefore']=-5
        with self.assertRaises(ValueError):apple.validate(r)
        apple.validate({'op':'update','app':'reminders','calendar':'x','id':'y','fields':{'remindAt':'2026-09-16T10:00:00-07:00'}})
        note={'op':'update','app':'notes','calendar':'x','id':'y','fields':{'text':'replacement'}}
        with self.assertRaises(ValueError):apple.validate(note)
        note['expectedModified']='2026-09-16T10:00:00Z';apple.validate(note)
        create_note={'op':'create','app':'notes','calendar':'x','token':str(uuid.uuid4()),'fields':{'title':'Title','appendText':'must not be lost'}}
        with self.assertRaises(ValueError):apple.validate(create_note)
        note['fields']['appendText']='extra'
        with self.assertRaises(ValueError):apple.validate(note)
    def test_container_requests_need_exact_source_and_name(self):
        apple.validate({'op':'create-container','app':'notes','source':'account-id','name':'A folder'})
        with self.assertRaises(ValueError):apple.validate({'op':'create-container','app':'notes','name':'A folder'})
        with self.assertRaises(ValueError):apple.validate({'op':'rename-container','app':'calendar','calendar':'id','name':' '})
    def test_all_day_and_bounded_query(self):
        r=self.event();r['fields'].update(allDay=True,start='2026-09-16T00:00:00-07:00',end='2026-09-17T00:00:00-07:00');apple.validate(r)
        with self.assertRaises(ValueError):apple.validate({'op':'list','app':'calendar','calendar':'x','start':'2026-01-01T00:00:00Z','end':'2027-01-01T00:00:00Z'})

if __name__=='__main__': unittest.main()
