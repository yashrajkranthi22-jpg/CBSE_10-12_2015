"""Draw a schematic cylinder with a hemispherical cavity at each end."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import annotate, plot_curve, plot_label, plot_line

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# The figure is a side-view sketch. Curved dashed lines represent the cavities;
# the dimensions printed here match the question rather than the sketch scale.
length = 4.8
height = 2.4
radius = height / 2

fig, ax = plt.subplots(figsize=(5.7, 3.2))
plot_line(ax, (0, 0), (0, height), linewidth=1.7)
plot_line(ax, (length, 0), (length, height), linewidth=1.7)
plot_line(ax, (0, height), (length, height), linewidth=1.7)
plot_line(ax, (0, 0), (length, 0), linewidth=1.7)

# Draw only the inward-facing half-circles to suggest the scooped-out ends.
angles = np.linspace(-np.pi / 2, np.pi / 2, 120)
plot_curve(ax, radius + radius * np.cos(angles), radius + radius * np.sin(angles),
            linestyle="--", linewidth=1.3)
plot_curve(ax, length - radius * np.cos(angles), radius + radius * np.sin(angles),
            linestyle="--", linewidth=1.3)
annotate(ax, "", xy=(0, 2.7), xytext=(length, 2.7),
          arrowprops={"arrowstyle": "<->", "lw": 1})
plot_label(ax, length / 2, 2.82, "10 cm", ha="center", fontsize=9)
plot_label(ax, length / 2, -0.35, "outer radius = 4.2 cm", ha="center", fontsize=9)
plot_label(ax, 0.35, 1.2, "cavity", rotation=90, ha="center", fontsize=8)
plot_label(ax, length - 0.35, 1.2, "cavity", rotation=90, ha="center", fontsize=8)
ax.set_xlim(-0.5, length + 0.5)
ax.set_ylim(-0.55, 3.15)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "CylinderScooped.png", dpi=180, bbox_inches="tight")
plt.close(fig)
