"""Draw the tower-and-shadow diagram used in Q2."""
import math
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codes" / "CoordGeo"))
sys.path.insert(0, str(ROOT / "codes"))
from CoordGeo.line.funcs import line_gen

# These scaled coordinates preserve the right-triangle shape in the question.
height = 3.0
shadow = 3 * math.sqrt(3)
A = np.array([0.0, height])
B = np.array([0.0, 0.0])
C = np.array([shadow, 0.0])

def draw_segment(start, end, **style):
    points = line_gen(np.asarray(start, dtype=float), np.asarray(end, dtype=float))
    ax.plot(points[0], points[1], **style)

fig, ax = plt.subplots(figsize=(5.5, 3.2))
draw_segment(B, A, linewidth=2)            # Tower
draw_segment(B, C, linewidth=2)            # Ground/shadow
draw_segment(A, C, linewidth=1.8)           # Sun ray
ax.scatter([A[0], C[0]], [A[1], C[1]], s=20)

ax.text(-0.18, height / 2, "20 m", ha="right", va="center")
ax.text(shadow / 2, -0.28, r"$20\sqrt{3}$ m", ha="center")
ax.text(-0.10, -0.15, "B", ha="right")
ax.text(-0.10, height + 0.05, "A", ha="right")
ax.text(shadow + 0.07, -0.10, "C")
ax.text(0.35, 0.20, r"$\theta$", fontsize=11)

ax.set_xlim(-0.8, shadow + 0.5)
ax.set_ylim(-0.6, height + 0.5)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Tower.png", dpi=180, bbox_inches="tight")
plt.close(fig)
