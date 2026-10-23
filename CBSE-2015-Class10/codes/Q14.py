"""Draw the section-formula figure for Q14."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import plot_label, plot_line, plot_points

from CoordGeo.line.line import displacement

ROOT = Path(__file__).resolve().parents[1]

# P divides AB internally in the ratio 3:4, so it lies 3/7 of the way
# from A to B. This coordinate is included to show where P falls on the line.
A = (-2, -2)
B = (2, -4)
ratio_from_A = 3 / 7

# Use CoordGeo's displacement helper, then move 3/7 of the way from A to B.
# This gives the point that divides AB internally in the ratio 3:4.
dx, dy = displacement(A, B)
P = (A[0] + ratio_from_A * dx, A[1] + ratio_from_A * dy)

fig, ax = plt.subplots(figsize=(6, 3.8))
plot_line(ax, A, B, linewidth=2)
plot_points(ax, [A, P, B], s=28, zorder=3)
for name, point, dx, dy in [
    ("A", A, -0.2, 0.18), ("P", P, 0.05, 0.16), ("B", B, 0.06, -0.2)
]:
    label = f"{name} {point}" if name != "P" else name
    plot_label(ax, point[0] + dx, point[1] + dy, label, fontsize=9)
plot_label(ax, (A[0] + P[0]) / 2, (A[1] + P[1]) / 2 + 0.12,
         "3 parts", ha="center", fontsize=9)
plot_label(ax, (P[0] + B[0]) / 2, (P[1] + B[1]) / 2 - 0.25,
         "4 parts", ha="center", fontsize=9)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True, alpha=0.25)
ax.set_xlim(-2.6, 2.7)
ax.set_ylim(-4.8, -1.3)
fig.tight_layout()
fig.savefig(ROOT / "figs" / "SectionPoint.png", dpi=180, bbox_inches="tight")
plt.close(fig)
