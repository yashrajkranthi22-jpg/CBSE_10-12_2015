"""Draw the two flower-bed regions outside the square in Q30."""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import add_circle, add_rectangle, fill_polygon, plot_label, plot_line, plot_points

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# The square has side 42 m. Its half-diagonal gives the circle radius.
side = 42
half_side = side / 2
radius = half_side * math.sqrt(2)

fig, ax = plt.subplots(figsize=(5.8, 4.6))
add_circle(ax, (0, 0), radius, fill=False, edgecolor="black", linewidth=1.4)
add_rectangle(ax, (-half_side, -half_side), side, side,
              facecolor="white", edgecolor="black", linewidth=1.6, zorder=2)

# The circle meets the square at its corners. Sample the arcs to shade the
# circular pieces to the left and right of the square.
angle_limit = math.acos(half_side / radius)
angles = np.linspace(-angle_limit, angle_limit, 200)
right_arc = np.column_stack([radius * np.cos(angles), radius * np.sin(angles)])
right_region = np.vstack([right_arc, [half_side, half_side], [half_side, -half_side]])
fill_polygon(ax, right_region[:, 0], right_region[:, 1], color="#b8d9f2", alpha=0.95, zorder=1)
left_arc = np.column_stack([-radius * np.cos(angles), radius * np.sin(angles)])
left_region = np.vstack([left_arc, [-half_side, half_side], [-half_side, -half_side]])
fill_polygon(ax, left_region[:, 0], left_region[:, 1], color="#b8d9f2", alpha=0.95, zorder=1)

# Redraw the square so its border remains clearly visible over the shading.
add_rectangle(ax, (-half_side, -half_side), side, side,
              facecolor="white", edgecolor="black", linewidth=1.6, zorder=2)
plot_line(ax, (-half_side, -half_side), (half_side, half_side), linestyle=":", linewidth=1)
plot_line(ax, (-half_side, half_side), (half_side, -half_side), linestyle=":", linewidth=1)
plot_points(ax, [(0, 0)], s=18, zorder=4)
plot_label(ax, 0.7, 0.9, "O", fontsize=9)
plot_label(ax, 0, -half_side - 2.8, "42 m", ha="center", fontsize=9)
plot_label(ax, half_side + 4, 0, "bed", rotation=90, ha="center", fontsize=9)
plot_label(ax, -half_side - 4, 0, "bed", rotation=90, ha="center", fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-radius - 5, radius + 5)
ax.set_ylim(-radius - 6, radius + 5)
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "FlowerBeds.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# Using pi = 22/7, total shaded area = two 90-degree sectors minus two
# triangles with base and height 21 m: 441*pi - 2*(1/2*21*21) = 504 m^2.
shaded_area = 441 * (22 / 7) - 882
assert math.isclose(shaded_area, 504, abs_tol=1e-12)
print(f"Q30: total shaded area={shaded_area:.0f} m^2")
