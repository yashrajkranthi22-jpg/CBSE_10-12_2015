"""Draw the triangle and incircle for Q6."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import add_circle, plot_curve, plot_label, plot_line, plot_points


ROOT = Path(__file__).resolve().parents[1]

# A 9-12-15 right triangle is used. Its inradius is 3 cm, and the touch point
# D splits the 15 cm base into BD = 6 cm and DC = 9 cm.
A = (5.4, 7.2)
B = (0.0, 0.0)
C = (15.0, 0.0)
D = (6.0, 0.0)
O = (6.0, 3.0)
F = (3.6, 4.8)  # Touch point on AB: BF = 6 cm and AF = 3 cm.
E = (7.8, 5.4)  # Touch point on AC: CE = 9 cm and AE = 3 cm.
radius = 3.0

fig, ax = plt.subplots(figsize=(6.2, 4.1))
plot_curve(ax, [B[0], A[0], C[0], B[0]], [B[1], A[1], C[1], B[1]],
           color="black", linewidth=1.7)
add_circle(ax, O, radius, fill=False, edgecolor="black", linewidth=1.6)

# A radius is perpendicular to a tangent at the touch point.
for point in (D, E, F):
    plot_line(ax, O, point, color="0.35", linestyle="--", linewidth=1.0)
# Right-angle marker where OD meets the base.
plot_curve(ax, [D[0], D[0] + 0.35, D[0] + 0.35], [0.35, 0.35, 0],
           color="black", linewidth=0.8)
plot_points(ax, [A, B, C, D, O, E, F],
           s=12, color="black", zorder=3)

labels = {
    "A": (A, 0.08, 0.10), "B": (B, -0.35, -0.36),
    "C": (C, 0.10, -0.36), "D": (D, -0.05, -0.40),
    "O": (O, -0.42, -0.02), "E": (E, 0.12, 0.08),
    "F": (F, -0.30, 0.06),
}
for name, (point, dx, dy) in labels.items():
    plot_label(ax, point[0] + dx, point[1] + dy, name, fontsize=9.5)

plot_label(ax, 2.7, -0.58, "6 cm", ha="center", fontsize=9.5)
plot_label(ax, 10.5, -0.58, "9 cm", ha="center", fontsize=9.5)
plot_label(ax, 6.18, 1.58, r"$3\,\mathrm{cm}$", fontsize=9.5)
ax.set_xlim(-1, 16.1)
ax.set_ylim(-0.9, 8.7)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")
fig.tight_layout(pad=0.2)
fig.savefig(ROOT / "figs" / "IncircleTriangle.png", dpi=210, bbox_inches="tight")
plt.close(fig)
print("Q6 figure generated: all three sides touch the radius-3 cm circle.")
