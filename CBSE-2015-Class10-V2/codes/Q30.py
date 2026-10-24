"""Draw the two flower-bed regions outside the square in Q30."""
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
from CoordGeo.conics.funcs import circ_arc, circ_gen
from CoordGeo.line.funcs import line_gen

# The square has side 42 m. Its half-diagonal gives the circle radius.
side = 42
half_side = side / 2
radius = half_side * math.sqrt(2)
centre = np.array([0.0, 0.0])

fig, ax = plt.subplots(figsize=(5.8, 4.6))
# Use CoordGeo's functions for the circle and the two arcs bordering the beds.
circle = circ_gen(centre, radius)
ax.plot(circle[0], circle[1], color="black", linewidth=1.4)
ax.add_patch(plt.Rectangle((-half_side, -half_side), side, side,
                           facecolor="white", edgecolor="black", linewidth=1.6, zorder=2))

angle_limit = math.degrees(math.acos(half_side / radius))
right_arc = circ_arc(centre, radius, -angle_limit, angle_limit, 200)
left_arc = circ_arc(centre, radius, 180 + angle_limit, 180 - angle_limit, 200)
right_region = np.column_stack((
    np.r_[right_arc[0], half_side, half_side],
    np.r_[right_arc[1], half_side, -half_side],
))
left_region = np.column_stack((
    np.r_[left_arc[0], -half_side, -half_side],
    np.r_[left_arc[1], half_side, -half_side],
))
ax.fill(right_region[:, 0], right_region[:, 1], color="#b8d9f2", alpha=0.95, zorder=1)
ax.fill(left_region[:, 0], left_region[:, 1], color="#b8d9f2", alpha=0.95, zorder=1)

# Redraw the square so its border is clear over the shading.
ax.add_patch(plt.Rectangle((-half_side, -half_side), side, side,
                           facecolor="white", edgecolor="black", linewidth=1.6, zorder=2))
for start, end in (
    ((-half_side, -half_side), (half_side, half_side)),
    ((-half_side, half_side), (half_side, -half_side)),
):
    points = line_gen(np.asarray(start, dtype=float), np.asarray(end, dtype=float))
    ax.plot(points[0], points[1], linestyle=":", linewidth=1)
ax.scatter([0], [0], s=18, zorder=4)
ax.text(0.7, 0.9, "O", fontsize=9)
ax.text(0, -half_side - 2.8, "42 m", ha="center", fontsize=9)
ax.text(half_side + 4, 0, "bed", rotation=90, ha="center", fontsize=9)
ax.text(-half_side - 4, 0, "bed", rotation=90, ha="center", fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-radius - 5, radius + 5)
ax.set_ylim(-radius - 6, radius + 5)
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "FlowerBeds.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# Using pi = 22/7, total shaded area = 441*pi - 2*(1/2*21*21) = 504 m^2.
shaded_area = 441 * (22 / 7) - 882
assert math.isclose(shaded_area, 504, abs_tol=1e-12)
print(f"Q30: total shaded area={shaded_area:.0f} m^2")
