"""Solve Q27 and draw the cloud/reflection diagram."""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import add_arc, plot_label, plot_line, plot_points

from CoordGeo.line.line import displacement
from CoordGeo.matrix.matrix import inner_product

ROOT = Path(__file__).resolve().parents[1]

# Let x be the horizontal distance from A to the point below the cloud, and H
# the cloud's height above the lake. A is 20 m above the lake.
# From the 30-degree line: H - 20 = x / sqrt(3).
# From the 60-degree line to the reflection: H + 20 = sqrt(3) * x.
# Solving these gives x = 20*sqrt(3) and H = 40 m.
# These are the values obtained from the trigonometric equations in the solution.
x = 20 * math.sqrt(3)
cloud_height = 40.0

A = (0.0, 20.0)
cloud = (x, cloud_height)
reflection = (x, -cloud_height)

# CoordGeo represents the line from A to the cloud as a displacement vector.
# Its dot product with itself is the square of the line's length.
AC_vector = displacement(A, cloud)
AC = math.sqrt(inner_product(AC_vector, AC_vector))

fig, ax = plt.subplots(figsize=(6.4, 4.3))
# The lake surface is y=0. The dashed horizontal marks the level of A.
plot_line(ax, (-5, 0), (x + 12, 0), color="black", linewidth=1.4)
plot_label(ax, x + 2.7, -3.2, "lake surface", fontsize=8.5)
plot_line(ax, (-3.5, A[1]), (x + 8, A[1]), color="0.25", linewidth=1.15, linestyle="--")
plot_label(ax, x * 0.78, A[1] + 3.5, "horizontal reference", ha="center", fontsize=8.2)
plot_line(ax, (0, 0), (0, 20), color="black", linestyle=":", linewidth=1.0)
plot_label(ax, -3.7, 8.0, "20 m", rotation=90, fontsize=9)

# Draw the two sight lines and the vertical line through the cloud/reflection.
plot_line(ax, A, cloud, color="black", linewidth=1.55)
plot_line(ax, A, reflection, color="black", linewidth=1.55)
plot_line(ax, (x, -cloud_height), (x, cloud_height), color="0.35", linestyle=":", linewidth=1.0)
plot_points(ax, [A, cloud, reflection], s=20, color="black", zorder=4)
plot_label(ax, -1.25, 21.3, "A", fontsize=10)
plot_label(ax, x + 1.0, cloud_height + 1.1, "cloud", fontsize=9)
plot_label(ax, x + 1.0, -cloud_height - 3.6, "reflection", fontsize=9)
add_arc(ax, A, 15, 15, angle=0, theta1=0, theta2=30, color="black", linewidth=1.0)
add_arc(ax, A, 17, 17, angle=0, theta1=-60, theta2=0, color="black", linewidth=1.0)
plot_label(ax, 7.5, 27.0, r"$30^\circ$", fontsize=9.5)
plot_label(ax, 7.8, 12.3, r"$60^\circ$", fontsize=9.5)
plot_label(ax, x * 0.63, 8.0, r"$x=20\sqrt{3}\,\mathrm{m}$", ha="center", fontsize=8.8)
ax.set_xlim(-5, x + 13)
ax.set_ylim(-cloud_height - 8, cloud_height + 8)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")
fig.tight_layout(pad=0.2)
fig.savefig(ROOT / "figs" / "CloudReflection.png", dpi=210, bbox_inches="tight")
plt.close(fig)
print(f"Q27: plotted x=20*sqrt(3) m, cloud height=40 m; CoordGeo gives AC={AC:.2f} m.")
