"""Solve Q27 and draw the cloud/reflection diagram using CoordGeo geometry functions."""
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
from CoordGeo.conics.funcs import circ_arc
from CoordGeo.line.funcs import dir_vec, line_gen

# Let x be the horizontal distance from A to the point below the cloud, and H its height.
# The trigonometric equations give x = 20*sqrt(3) and H = 40 m.
x = 20 * math.sqrt(3)
cloud_height = 40.0
A = np.array([0.0, 20.0])
cloud = np.array([x, cloud_height])
reflection = np.array([x, -cloud_height])

# CoordGeo supplies the displacement vector; its norm is the sight-line distance AC.
AC_vector = dir_vec(A, cloud)
AC = np.linalg.norm(AC_vector)

fig, ax = plt.subplots(figsize=(6.4, 4.3))
def draw_segment(start, end, **style):
    points = line_gen(np.asarray(start, dtype=float), np.asarray(end, dtype=float))
    ax.plot(points[0], points[1], **style)

# The lake is y=0; the dashed line shows the level of A.
draw_segment((-5, 0), (x + 12, 0), color="black", linewidth=1.4)
ax.text(x + 2.7, -3.2, "lake surface", fontsize=8.5)
draw_segment((-3.5, A[1]), (x + 8, A[1]), color="0.25", linewidth=1.15, linestyle="--")
ax.text(x * 0.78, A[1] + 3.5, "horizontal reference", ha="center", fontsize=8.2)
draw_segment((0, 0), (0, 20), color="black", linestyle=":", linewidth=1.0)
ax.text(-3.7, 8.0, "20 m", rotation=90, fontsize=9)

# Sight lines, the vertical cloud/reflection line, and the angle arcs.
draw_segment(A, cloud, color="black", linewidth=1.55)
draw_segment(A, reflection, color="black", linewidth=1.55)
draw_segment((x, -cloud_height), (x, cloud_height), color="0.35", linestyle=":", linewidth=1.0)
ax.scatter([A[0], cloud[0], reflection[0]],
           [A[1], cloud[1], reflection[1]], s=20, color="black", zorder=4)
ax.text(-1.25, 21.3, "A", fontsize=10)
ax.text(x + 1.0, cloud_height + 1.1, "cloud", fontsize=9)
ax.text(x + 1.0, -cloud_height - 3.6, "reflection", fontsize=9)
arc_30 = circ_arc(A, 15, 0, 30, 50)
arc_60 = circ_arc(A, 17, -60, 0, 50)
ax.plot(arc_30[0], arc_30[1], color="black", linewidth=1.0)
ax.plot(arc_60[0], arc_60[1], color="black", linewidth=1.0)
ax.text(7.5, 27.0, r"$30^\circ$", fontsize=9.5)
ax.text(7.8, 12.3, r"$60^\circ$", fontsize=9.5)
ax.text(x * 0.63, 8.0, r"$x=20\sqrt{3}\,\mathrm{m}$", ha="center", fontsize=8.8)
ax.set_xlim(-5, x + 13)
ax.set_ylim(-cloud_height - 8, cloud_height + 8)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")
fig.tight_layout(pad=0.2)
fig.savefig(ROOT / "figs" / "CloudReflection.png", dpi=210, bbox_inches="tight")
plt.close(fig)
print(f"Q27: plotted x=20*sqrt(3) m, cloud height=40 m; CoordGeo gives AC={AC:.2f} m.")
