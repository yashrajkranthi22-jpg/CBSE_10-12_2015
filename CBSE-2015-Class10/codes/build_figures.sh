#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# Execute the separate question-specific scripts in one Python process so
# Matplotlib is imported only once; each script remains independently runnable.
python3 - "$ROOT" <<'PY'
from pathlib import Path
import runpy
import sys
root = Path(sys.argv[1]).resolve()
# Make the bundled CoordGeo library importable during runpy execution.
sys.path.insert(0, str(root / "codes"))
scripts = [
    "QLogo.py", "Q01.py", "Q02.py", "Q03.py", "Q04.py", "Q06.py",
    "Q13.py", "Q14.py", "Q15.py", "Q16.py", "Q17.py", "Q27.py",
    "Q29.py", "Q30.py", "Q31.py",
]
for script in scripts:
    print(f"=== {script} ===", flush=True)
    runpy.run_path(str(root / "codes" / script), run_name="__main__")
PY
