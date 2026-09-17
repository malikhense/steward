import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
def run(root,*args):return subprocess.run(['python3',str(root/'scripts/install.py'),*map(str,args)],capture_output=True,text=True)

class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.folder=Path(self.temp.name).resolve();self.source=self.folder/'source'
        shutil.copytree(ROOT,self.source,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
        self.dest=self.folder/'installed'
    def test_managed_update_backs_up_and_preserves_local_edits(self):
        p=run(self.source,'--dest',self.dest,'--apply');self.assertEqual(p.returncode,0,p.stderr)
        skill=self.source/'skills/steward/SKILL.md';skill.write_text(skill.read_text()+'\nVersion two fixture.\n')
        preview=run(self.source,'--dest',self.dest,'--update');self.assertEqual(preview.returncode,0,preview.stderr)
        self.assertEqual(json.loads(preview.stdout)['updating'],['steward'])
        original=(self.dest/'steward/SKILL.md').read_text()
        p=run(self.source,'--dest',self.dest,'--update','--apply');self.assertEqual(p.returncode,0,p.stderr)
        with zipfile.ZipFile(json.loads(p.stdout)['backup']) as z:self.assertEqual(z.read('steward/SKILL.md').decode(),original)
        installed=self.dest/'steward/SKILL.md';installed.write_text(installed.read_text()+'\nUser edit.\n');before=installed.read_text()
        skill.write_text(skill.read_text()+'\nVersion three fixture.\n')
        self.assertNotEqual(run(self.source,'--dest',self.dest,'--update','--apply').returncode,0)
        self.assertEqual(installed.read_text(),before)
    def test_package_contains_complete_runtime_and_no_local_state(self):
        (self.source/'private').mkdir();(self.source/'private/secret.txt').write_text('synthetic excluded data')
        (self.source/'.env').write_text('SYNTHETIC=excluded')
        out=self.folder/'package'
        p=subprocess.run(['python3',str(self.source/'scripts/package.py'),'--out',str(out)],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        result=json.loads(p.stdout);archive=Path(result['archive'])
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(),result['sha256'])
        with zipfile.ZipFile(archive) as z:
            names=z.namelist();self.assertEqual(len([n for n in names if n.endswith('/SKILL.md')]),16)
            self.assertIn('steward/.codex-plugin/plugin.json',names)
            self.assertFalse(any('/private/' in n or '/.env' in n or '/.git/' in n for n in names))
        # The extracted deliverable can install itself without the repository.
        installed=self.folder/'from-package'
        p=run(out/'steward','--dest',installed,'--apply');self.assertEqual(p.returncode,0,p.stderr)

    def test_legacy_migration_is_backed_up_and_local_edits_block_it(self):
        legacy=self.folder/'legacy'
        shutil.copytree(self.source,legacy)
        for folder in (legacy/'skills').glob('steward-*'):
            if folder.name=='steward-apple': continue
            oldname=folder.name.replace('steward-','kernel-',1)
            entry=folder/'SKILL.md'
            entry.write_text(entry.read_text().replace('name: '+folder.name,'name: '+oldname))
            folder.rename(folder.with_name(oldname))
        # This synthetic prior package only needs an installer preflight.
        (legacy/'scripts/check.py').write_text('print("synthetic old package")')
        p=run(legacy,'--dest',self.dest,'--apply');self.assertEqual(p.returncode,0,p.stderr)
        entry=self.dest/'kernel-goals/SKILL.md';original=entry.read_text()
        entry.write_text(original+'\nLocal edit\n')
        p=run(self.source,'--dest',self.dest,'--update','--apply')
        self.assertNotEqual(p.returncode,0);self.assertFalse((self.dest/'steward-goals').exists())
        entry.write_text(original)
        p=run(self.source,'--dest',self.dest,'--update');self.assertEqual(p.returncode,0,p.stderr)
        self.assertTrue(entry.exists())
        p=run(self.source,'--dest',self.dest,'--update','--apply');self.assertEqual(p.returncode,0,p.stderr)
        result=json.loads(p.stdout)
        self.assertFalse(entry.exists());self.assertTrue((self.dest/'steward-goals/SKILL.md').exists())
        with zipfile.ZipFile(result['backup']) as z:self.assertEqual(z.read('kernel-goals/SKILL.md').decode(),original)
        self.assertEqual(len(list(self.dest.glob('*/SKILL.md'))),16)
