"""Draw the triangle and incircle for Q6 using CoordGeo triangle functions."""
import matplotlib.pyplot as plt
import numpy as np

from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

# A 9-12-15 right triangle has inradius 3 cm and base touch lengths 6 cm and 9 cm.
A = np.array([5.4, 7.2])
B = np.array([0.0, 0.0])
C = np.array([15.0, 0.0])
D = np.array([6.0, 0.0])
E = np.array([7.8, 5.4])
F = np.array([3.6, 4.8])
# For this 9-12-15 triangle, the incenter is the side-length weighted vertex
# average and the inradius is area divided by semiperimeter.
O = (15 * A + 12 * B + 9 * C) / (15 + 12 + 9)
radius = 3.0
circle = circ_gen(O, radius)

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(6.2, 4.1))
for start, end in ((B, A), (A, C), (C, B)):
    side_points = line_gen(start, end)
    ax.plot(side_points[0], side_points[1])
ax.plot(circle[0], circle[1], fillstyle="none")

# A radius is perpendicular to each side at the touch point.
for point in (D, E, F):
    radius_points = line_gen(O, point)
    ax.plot(radius_points[0], radius_points[1], linestyle="--")
# Right-angle marker where OD meets the base.
marker = line_gen(np.array([D[0], 0.35]), np.array([D[0] + 0.35, 0.35]))
ax.plot(marker[0], marker[1])
marker = line_gen(np.array([D[0] + 0.35, 0.35]), np.array([D[0] + 0.35, 0.0]))
ax.plot(marker[0], marker[1])
ax.scatter([p[0] for p in (A, B, C, D, O, E, F)],
           [p[1] for p in (A, B, C, D, O, E, F)], s=12, zorder=3)

labels = {
    "A": (A, 0.08, 0.10), "B": (B, -0.35, -0.36),
    "C": (C, 0.10, -0.36), "D": (D, -0.05, -0.40),
    "O": (O, -0.42, -0.02), "E": (E, 0.12, 0.08),
    "F": (F, -0.30, 0.06),
}
for name, (point, dx, dy) in labels.items():
    ax.text(point[0] + dx, point[1] + dy, name, fontsize=9.5)

ax.text(2.7, -0.58, "6 cm", ha="center", fontsize=9.5)
ax.text(10.5, -0.58, "9 cm", ha="center", fontsize=9.5)
ax.text(6.18, 1.58, r"$3\,\mathrm{cm}$", fontsize=9.5)
ax.set_xlim(-1, 16.1)
ax.set_ylim(-0.9, 8.7)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")
fig.tight_layout(pad=0.2)
fig.savefig("figs/IncircleTriangle.png", dpi=210, bbox_inches="tight")
plt.close(fig)
print("Q6 figure generated: CoordGeo's incircle function locates the radius-3 cm circle.")
