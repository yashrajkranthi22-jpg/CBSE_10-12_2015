#!/usr/bin/env python3
"""Structural and policy checks for the combined CBSE 2015 source."""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASS10 = ROOT / "CBSE-2015-Class10-Updated-corrected_V3"
CLASS12 = ROOT / "CBSE-2015-Class12-Updated-corrected_V3"

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()

def check(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")
    print(f"PASS: {message}")

main = (ROOT / "main.tex").read_text()
q10 = (CLASS10 / "chapters/class10.tex").read_text()
q12 = (CLASS12 / "chapters/class12.tex").read_text()
f10 = (CLASS10 / "chapters/class10_formulae.tex").read_text()
f12 = (CLASS12 / "chapters/class12_formulae.tex").read_text()

check(r"\section{Class 10 Mathematics 2015}" in main and
      r"\section{Class 12 Mathematics 2015}" in main,
      "combined document has the two required top-level class sections")
for title in ("Formulae", "Problems"):
    check(main.count(r"\subsection{" + title + "}") == 2,
          f"both class sections contain a {title} subsection")

for src_name, src in (("Class 10 questions", q10), ("Class 12 questions", q12)):
    check(not re.search(r"\\item\[\\textbf\{1\.2\.\d+\}\]", src),
          f"{src_name} uses enumerate-generated question numbers")
for src_name, src in (("Class 10 formulae", f10), ("Class 12 formulae", f12)):
    check(not re.search(r"\\(?:tag|tag\*)\{1\.1\.", src),
          f"{src_name} uses automatic equation numbering")
    check(not re.search(r"\\textbf\{1\.1\.\d+\}", src),
          f"{src_name} uses enumerate-generated formula-group numbers")

check("A train travels 54 km" not in q10, "excluded C10-Q23 is absent")
for term in ("Find the integrating factor of", "family $(x-h)",
             "is homogeneous and solve it", "A man speaks truth 3 out of 5 times"):
    check(term not in q12, f"excluded Class 12 production item is absent: {term}")

check("finite-support discrete-time signal" in q10 and
      r"\label{eq:finite-z-22}" in f10,
      "C10-Q22 finite Z-transform derivation and formula are linked")
check("unilateral Laplace transforms" in q12 and
      r"\label{eq:laplace-24}" in f12,
      "C12-Q24 transformed-coordinate Laplace derivation and formula are linked")
check("Clarke generalized derivatives" in q12 and
      r"\label{eq:nonsmooth-characteristic-48}" in f12,
      "C12-Q48 nonsmooth characteristic derivation and formula are linked")

expected_styles = {
    ROOT / "gvv.sty": "eb76e1531e65e97aeca5a5e32ce485816576555f",
    ROOT / "gvv-book.sty": "a2eefde9008baea7a2073ffba04b02757fd6ef42",
    CLASS10 / "gvv.sty": "eb76e1531e65e97aeca5a5e32ce485816576555f",
    CLASS10 / "gvv-book.sty": "a2eefde9008baea7a2073ffba04b02757fd6ef42",
    CLASS12 / "gvv.sty": "eb76e1531e65e97aeca5a5e32ce485816576555f",
    CLASS12 / "gvv-book.sty": "a2eefde9008baea7a2073ffba04b02757fd6ef42",
}
for path, expected in expected_styles.items():
    check(path.exists() and git_blob_sha(path) == expected,
          f"{path.relative_to(ROOT)} matches the reference blob")

with (ROOT / "audit/ADVANCED_METHOD_MAP.csv").open(newline="") as stream:
    rows = list(csv.DictReader(stream))
check(len(rows) == 38, "method map contains all 38 supplied rows")
check(sum(row["status"] == "EXCLUDED" for row in rows) == 5,
      "all five production exclusions are recorded")
check(sum(row["status"] == "PENDING_REWRITE" for row in rows) > 0,
      "unfinished method migrations remain visibly marked as pending")

labels = re.findall(r"\\label\{([^}]+)\}", q10 + "\n" + q12 + "\n" + f10 + "\n" + f12)
duplicates = sorted({label for label in labels if labels.count(label) > 1})
check(not duplicates, "equation and figure labels are unique across both classes")
print(f"Audit status: {sum(r['status']=='UPDATED' for r in rows)} updated, "
      f"{sum(r['status']=='EXCLUDED' for r in rows)} excluded, "
      f"{sum(r['status']=='PENDING_REWRITE' for r in rows)} pending.")
