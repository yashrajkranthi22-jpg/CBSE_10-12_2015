"""Draw the circular segments and check their areas for Q16."""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import add_circle, add_polygon, add_wedge, annotate, plot_label, plot_line


ROOT = Path(__file__).resolve().parents[1]

# A 60-degree sector of a circle with radius 14 cm forms the minor segment.
# The diagram is drawn at unit radius so the labels fit neatly.
radius = 1.0
P1 = (math.cos(math.radians(30)), math.sin(math.radians(30)))
P2 = (math.cos(math.radians(30)), -math.sin(math.radians(30)))

fig, ax = plt.subplots(figsize=(5.2, 4.2))
add_circle(ax, (0, 0), radius, facecolor="none", edgecolor="black", linewidth=1.5)
add_wedge(ax, (0, 0), radius, -30, 30,
              facecolor="#b8d9f2", edgecolor="none", alpha=0.95)
add_polygon(ax, [(0, 0), P1, P2], closed=True,
                facecolor="white", edgecolor="black", linewidth=1.3)
plot_line(ax, (0, 0), P1, color="black", linestyle="--", linewidth=1)
plot_line(ax, (0, 0), P2, color="black", linestyle="--", linewidth=1)
plot_line(ax, P1, P2, color="black", linestyle="-", linewidth=1.4)
plot_label(ax, 0.43, 0.05, r"$60^\circ$", fontsize=9)
annotate(ax, "minor segment", xy=(0.97, 0.02), xytext=(1.16, 0.23),
          fontsize=8, ha="left", arrowprops={"arrowstyle": "->", "lw": 0.8})
plot_label(ax, -0.45, -0.35, "major segment\n(remainder)", fontsize=8, ha="center")
plot_label(ax, 0.12, 0.52, "14 cm", fontsize=8, rotation=30)
ax.set_aspect("equal")
ax.set_xlim(-1.25, 1.55)
ax.set_ylim(-1.18, 1.2)
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "SegmentAreas.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# Area of the two shaded minor parts together: two 90-degree sectors minus
# the two right triangles between the radii and the sides of the square.
minor_and_major_total = 616
minor_area = 308 / 3 - 49 * math.sqrt(3)
major_area = minor_and_major_total - minor_area
assert math.isclose(minor_area + major_area, minor_and_major_total, abs_tol=1e-12)
print(f"Q16: minor segment={minor_area:.4f} cm^2; major segment={major_area:.4f} cm^2")
