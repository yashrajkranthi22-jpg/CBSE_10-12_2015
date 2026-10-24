"""Draw the schematic chord-and-tangent figure for Q4."""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codes" / "CoordGeo"))
sys.path.insert(0, str(ROOT / "codes"))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

# A unit circle keeps this geometric illustration simple.
O = np.array([0.0, 0.0])
circle = circ_gen(O, 1.0)
P = np.array([0.0, -1.0])
Q = np.array([np.cos(np.pi / 6), np.sin(np.pi / 6)])
R = np.array([np.cos(-np.pi / 3), np.sin(-np.pi / 3)])
T = np.array([1.8, -1.0])

fig, ax = plt.subplots(figsize=(5.3, 3.7))
ax.plot(circle[0], circle[1], linewidth=1.5)

# CoordGeo generates the line segments; these styles distinguish radii and chords.
segments = [(P, Q, "-"), (P, R, "-"), (Q, R, "-"),
            (O, P, "--"), (O, Q, "--"), (P, T, "-")]
for start, end, style in segments:
    points = line_gen(start, end)
    ax.plot(points[0], points[1], linestyle=style, linewidth=1.25)

labels = [("O", O, -0.12, 0.10), ("P", P, -0.18, -0.12),
          ("Q", Q, 0.04, 0.05), ("R", R, 0.05, -0.05),
          ("T", T, 0.03, -0.05)]
for name, point, dx, dy in labels:
    ax.text(point[0] + dx, point[1] + dy, name, fontsize=10)

ax.text(0.25, -0.72, r"$60^\circ$", fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-1.35, 2.0)
ax.set_ylim(-1.5, 1.45)
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "TangentChord.png", dpi=180, bbox_inches="tight")
plt.close(fig)
