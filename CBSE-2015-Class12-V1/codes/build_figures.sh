#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# Each plotting script uses derived values and only checks the stated conditions.
for script in Q01.py Q05.py Q06.py Q10.py Q15.py Q46.py Q47.py Q48.py Q52.py Q53.py Q55.py Q59.py Q60.py Q64.py Q65.py; do
  python3 "codes/$script"
done
