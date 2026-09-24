"""Run the standard-library contract suite without installing provider SDKs."""
from pathlib import Path
import json
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
for component in json.loads((ROOT / "docs/REPO_MAP.json").read_text())["components"]:
    sys.path.insert(0, str(ROOT / component["path"] / "src"))
suite = unittest.defaultTestLoader.discover(str(ROOT / "tests/contracts"))
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
