"""Draw the cross-section of the cylinder-and-cone tent in Q17."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import plot_label, plot_line


ROOT = Path(__file__).resolve().parents[1]

# This is a schematic cross-section, not a scale drawing. The labels carry
# the measurements used in the solution.
radius = 1.4
base_y = 0
cylinder_height = 2.0
cone_height = 1.4
peak_y = cylinder_height + cone_height

fig, ax = plt.subplots(figsize=(5.0, 3.7))
plot_line(ax, (-radius, base_y), (-radius, cylinder_height), linewidth=1.6)
plot_line(ax, (radius, base_y), (radius, cylinder_height), linewidth=1.6)
plot_line(ax, (-radius, base_y), (radius, base_y), linewidth=1.6)
plot_line(ax, (-radius, cylinder_height), (0, peak_y), linewidth=1.6)
plot_line(ax, (0, peak_y), (radius, cylinder_height), linewidth=1.6)
plot_line(ax, (-radius, cylinder_height), (radius, cylinder_height), linestyle=":", linewidth=1)
plot_label(ax, radius + 0.15, 1.0, "4 m", va="center", fontsize=9)
plot_label(ax, 0.1, cylinder_height + cone_height * 0.55, "2.8 m", fontsize=9)
plot_label(ax, 0, -0.28, "4.2 m diameter", ha="center", fontsize=9)
ax.set_xlim(-2, 2)
ax.set_ylim(-0.55, 3.8)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Tent.png", dpi=180, bbox_inches="tight")
plt.close(fig)
