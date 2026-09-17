import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SETUP = ROOT / 'skills/steward-session/scripts/setup_memory.py'
INSTALL = ROOT / 'scripts/install.py'


def run(script, *args):
    return subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True, text=True)


def snapshot(path):
    return {str(p.relative_to(path)): p.read_bytes() for p in path.rglob('*') if p.is_file()}


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def test_preview_creates_nothing(self):
        vault = self.root / 'vault'
        r = run(SETUP, '--vault', vault)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(vault.exists())

    def test_create_readback_and_repeat_preserve_human_edits(self):
        vault = self.root / 'vault'
        r = run(SETUP, '--vault', vault, '--apply')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout)['onboarding'], 'not-started')
        (vault / 'Home.md').write_text('Human edited home\n')
        before = snapshot(vault)
        r = run(SETUP, '--vault', vault, '--apply')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(before, snapshot(vault))
        self.assertEqual(json.loads(r.stdout)['state'], 'existing-scaffold')

    def test_existing_vault_preserved(self):
        vault = self.root / 'vault'; vault.mkdir()
        (vault / 'notes.md').write_text('Existing human notes')
        before = snapshot(vault)
        self.assertNotEqual(run(SETUP, '--vault', vault, '--apply').returncode, 0)
        self.assertEqual(before, snapshot(vault))

    def test_partial_scaffold_preserved(self):
        vault = self.root / 'vault'
        self.assertEqual(run(SETUP, '--vault', vault, '--apply').returncode, 0)
        (vault / 'Home.md').unlink()
        before = snapshot(vault)
        self.assertNotEqual(run(SETUP, '--vault', vault, '--apply').returncode, 0)
        self.assertEqual(before, snapshot(vault))

    def test_symlink_vault_preserved(self):
        target = self.root / 'actual'; target.mkdir()
        link = self.root / 'link'; link.symlink_to(target)
        self.assertNotEqual(run(SETUP, '--vault', link, '--apply').returncode, 0)
        self.assertEqual(list(target.iterdir()), [])

    def test_install_preview_then_repeat(self):
        dest = self.root / 'skills'
        self.assertEqual(run(INSTALL, '--dest', dest).returncode, 0)
        self.assertFalse(dest.exists())
        r = run(INSTALL, '--dest', dest, '--apply')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(len(list(dest.glob('*/SKILL.md'))), 16)
        before = snapshot(dest)
        self.assertEqual(run(INSTALL, '--dest', dest, '--apply').returncode, 0)
        self.assertEqual(before, snapshot(dest))

    def test_install_conflict_stops_before_other_copies(self):
        dest = self.root / 'skills'; existing = dest / 'steward-memory'; existing.mkdir(parents=True)
        (existing / 'SKILL.md').write_text('User version')
        before = snapshot(dest)
        self.assertNotEqual(run(INSTALL, '--dest', dest, '--apply').returncode, 0)
        self.assertEqual(before, snapshot(dest))


if __name__ == '__main__':
    unittest.main()
