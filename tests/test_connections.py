import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills/steward-session/scripts/connections.py'
spec=importlib.util.spec_from_file_location('connections',SCRIPT)
connection=importlib.util.module_from_spec(spec);spec.loader.exec_module(connection)

class ConnectionsTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.vault=Path(self.temp.name).resolve();self.path=connection.registry_path(self.vault)
    def args(self,command,**kw):return argparse.Namespace(command=command,**kw)
    def select(self,v,*apps):
        connection.execute(self.args('select',apps=list(apps),context=True,scope='Relevant current task; private writes only'),v)
    def test_preview_and_status_create_no_files(self):
        for cmd in [['status'],['select','--apps','mail','--scope','Relevant commitments']]:
            p=subprocess.run(['python3',str(SCRIPT),'--vault',str(self.vault),*cmd],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stdout)
        self.assertEqual(list(self.vault.iterdir()),[])
    def test_choices_resume_and_skip_without_false_verification(self):
        v=connection.read(self.path);self.select(v,'calendar','mail')
        connection.execute(self.args('skip',apps=['notes']),v)
        connection.save(self.path,v,None)
        s=connection.status(connection.read(self.path))
        self.assertEqual(s['pending'],['calendar','mail'])
        self.assertFalse(s['connectionsReviewed'])
        self.assertEqual(next(x for x in s['apps'] if x['app']=='notes')['choice'],'skipped')
    def test_probe_requires_choice_and_saves_real_route_result(self):
        v=connection.read(self.path);a=self.args('probe',app='calendar')
        with self.assertRaises(ValueError):connection.execute(a,v)
        self.select(v,'calendar')
        result=subprocess.CompletedProcess([],0,json.dumps({'containers':[{'id':'synthetic','name':'Private'}]}),'')
        with patch.object(connection.subprocess,'run',return_value=result):
            response=connection.execute(a,v)
        self.assertEqual(response['state'],'verified')
        self.assertEqual(response['writes'],'not-established-by-this-read')
        self.assertEqual(v['apps']['calendar']['containers'][0]['id'],'synthetic')
    def test_denial_and_timeout_stay_pending(self):
        v=connection.read(self.path);self.select(v,'calendar')
        with patch.object(connection.subprocess,'run',return_value=subprocess.CompletedProcess([],1,'{"error":"permission denied"}','')):
            self.assertEqual(connection.execute(self.args('probe',app='calendar'),v)['state'],'blocked')
        with patch.object(connection.subprocess,'run',side_effect=subprocess.TimeoutExpired('connector',240)):
            self.assertEqual(connection.execute(self.args('probe',app='calendar'),v)['state'],'blocked')
        self.assertEqual(connection.status(v)['pending'],['calendar'])
    def test_ui_evidence_is_separate_from_connector_probe(self):
        v=connection.read(self.path);self.select(v,'mail','notes')
        with self.assertRaises(ValueError):connection.execute(self.args('probe',app='mail'),v)
        with self.assertRaises(ValueError):connection.execute(self.args('record-ui',app='notes',access='verified',evidence='fake',next=None),v)
        a=self.args('record-ui',app='mail',access='verified',evidence='Synthetic test fixture: selected account message list readable',next=None)
        self.assertEqual(connection.execute(a,v)['verification'],'host-observation-recorded')
    def test_disconnect_clears_metadata_and_reselect_needs_recheck(self):
        v=connection.read(self.path);self.select(v,'mail')
        connection.execute(self.args('record-ui',app='mail',access='verified',evidence='Synthetic observed list',next=None),v)
        connection.execute(self.args('disconnect',apps=['mail']),v)
        self.assertFalse(v['apps']['mail']['context']);self.assertIsNone(v['apps']['mail']['evidence'])
        self.select(v,'mail');self.assertEqual(v['apps']['mail']['access'],'unverified')
    def test_preserve_existing_content_symlinks_and_changed_registry(self):
        (self.vault/'Home.md').write_text('Human notes')
        v=connection.read(self.path);self.select(v,'calendar');connection.save(self.path,v,None)
        self.assertEqual((self.vault/'Home.md').read_text(),'Human notes')
        with self.assertRaises(ValueError):connection.save(self.path,v,None)
        link=self.vault/'alias';link.symlink_to(self.vault)
        with self.assertRaises(ValueError):connection.registry_path(link)

    def test_scope_change_requires_fresh_verification(self):
        v=connection.read(self.path);self.select(v,'mail')
        connection.execute(self.args('record-ui',app='mail',access='verified',evidence='Synthetic account observation',next=None),v)
        connection.execute(self.args('select',apps=['mail'],context=True,scope='Different account'),v)
        self.assertEqual(v['apps']['mail']['access'],'unverified')
        self.assertIsNone(v['apps']['mail']['evidence'])
