#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
chmod +x codes/build_figures.sh
./codes/build_figures.sh
# Numerical checks are deliberately split into question-specific scripts.
for script in Q08.py Q11.py Q22.py; do
  python3 "codes/$script"
done
# Build the PDF and retain the GVV/LaTeX support artifacts requested for the repository.
for pass in 1 2 3; do
  pdflatex -synctex=1 -recorder -interaction=nonstopmode -halt-on-error main.tex
  if [[ "$pass" == "1" ]]; then
    makeindex main.idx
    # This project has no printed index entries, but keep the companion file
    # from the GVV template's standard build set available in the repository.
    touch main.ind
  fi
done
