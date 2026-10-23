"""Draw the tower-and-shadow diagram used in Q2."""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import plot_label, plot_line, plot_points


ROOT = Path(__file__).resolve().parents[1]

# The labels give the real measurements; these shorter coordinates only make
# the drawing fit neatly on the page while keeping the same triangle shape.
height = 3.0
shadow = 3 * math.sqrt(3)

fig, ax = plt.subplots(figsize=(5.5, 3.2))
plot_line(ax, (0, 0), (0, height), linewidth=2)            # Tower
plot_line(ax, (0, 0), (shadow, 0), linewidth=2)            # Ground/shadow
plot_line(ax, (0, height), (shadow, 0), linewidth=1.8)     # Sun ray
plot_points(ax, [(0, height), (shadow, 0)], s=20)

plot_label(ax, -0.18, height / 2, "20 m", ha="right", va="center")
plot_label(ax, shadow / 2, -0.28, r"$20\sqrt{3}$ m", ha="center")
plot_label(ax, -0.10, -0.15, "B", ha="right")
plot_label(ax, -0.10, height + 0.05, "A", ha="right")
plot_label(ax, shadow + 0.07, -0.10, "C")
plot_label(ax, 0.35, 0.20, r"$\theta$", fontsize=11)

ax.set_xlim(-0.8, shadow + 0.5)
ax.set_ylim(-0.6, height + 0.5)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Tower.png", dpi=180, bbox_inches="tight")
plt.close(fig)
