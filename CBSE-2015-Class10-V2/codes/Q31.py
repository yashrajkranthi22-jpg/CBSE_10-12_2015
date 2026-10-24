"""Draw a schematic cylinder with a hemispherical cavity at each end."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# This side-view sketch is not a coordinate-geometry construction supported by
# CoordGeo, so retain direct Matplotlib drawing for the cylinder/cavity outline.
length = 4.8
height = 2.4
radius = height / 2

fig, ax = plt.subplots(figsize=(5.7, 3.2))
ax.plot([0, 0], [0, height], linewidth=1.7)
ax.plot([length, length], [0, height], linewidth=1.7)
ax.plot([0, length], [height, height], linewidth=1.7)
ax.plot([0, length], [0, 0], linewidth=1.7)

# Draw the inward-facing half-circles to suggest the scooped-out ends.
angles = np.linspace(-np.pi / 2, np.pi / 2, 120)
ax.plot(radius + radius * np.cos(angles), radius + radius * np.sin(angles),
        linestyle="--", linewidth=1.3)
ax.plot(length - radius * np.cos(angles), radius + radius * np.sin(angles),
        linestyle="--", linewidth=1.3)
ax.annotate("", xy=(0, 2.7), xytext=(length, 2.7),
            arrowprops={"arrowstyle": "<->", "lw": 1})
ax.text(length / 2, 2.82, "10 cm", ha="center", fontsize=9)
ax.text(length / 2, -0.35, "outer radius = 4.2 cm", ha="center", fontsize=9)
ax.text(0.35, 1.2, "cavity", rotation=90, ha="center", fontsize=8)
ax.text(length - 0.35, 1.2, "cavity", rotation=90, ha="center", fontsize=8)
ax.set_xlim(-0.5, length + 0.5)
ax.set_ylim(-0.55, 3.15)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "CylinderScooped.png", dpi=180, bbox_inches="tight")
plt.close(fig)
