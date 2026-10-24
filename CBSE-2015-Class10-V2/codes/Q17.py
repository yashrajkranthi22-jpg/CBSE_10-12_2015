"""Draw the cross-section of the cylinder-and-cone tent in Q17."""
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

# This is a schematic cross-section, not a scale drawing; the labels give the measurements.
radius = 1.4
base_y = 0
cylinder_height = 2.0
cone_height = 1.4
peak_y = cylinder_height + cone_height

fig, ax = plt.subplots(figsize=(5.0, 3.7))
segments = [
    ((-radius, base_y), (-radius, cylinder_height), "-", 1.6),
    ((radius, base_y), (radius, cylinder_height), "-", 1.6),
    ((-radius, base_y), (radius, base_y), "-", 1.6),
    ((-radius, cylinder_height), (0, peak_y), "-", 1.6),
    ((0, peak_y), (radius, cylinder_height), "-", 1.6),
    ((-radius, cylinder_height), (radius, cylinder_height), ":", 1.0),
]
for start, end, style, width in segments:
    points = line_gen(np.asarray(start, dtype=float), np.asarray(end, dtype=float))
    ax.plot(points[0], points[1], linestyle=style, linewidth=width)
ax.text(radius + 0.15, 1.0, "4 m", va="center", fontsize=9)
ax.text(0.1, cylinder_height + cone_height * 0.55, "2.8 m", fontsize=9)
ax.text(0, -0.28, "4.2 m diameter", ha="center", fontsize=9)
ax.set_xlim(-2, 2)
ax.set_ylim(-0.55, 3.8)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Tent.png", dpi=180, bbox_inches="tight")
plt.close(fig)
