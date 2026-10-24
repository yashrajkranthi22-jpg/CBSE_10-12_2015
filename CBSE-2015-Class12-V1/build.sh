#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
./codes/build_figures.sh
# These retained scripts verify theoretical results without solving the questions.
for script in Q24.py Q30.py Q37.py Q56.py Q57.py Q58.py; do
  printf '\n=== %s ===\n' "$script"
  python3 "codes/$script"
done
for pass in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  if [[ "$pass" == "1" ]]; then
    makeindex main.idx
  fi
done
