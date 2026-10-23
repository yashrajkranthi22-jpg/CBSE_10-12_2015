"""Plot the quadratic for the theoretically obtained value p = 3."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Save the graph directly to a file.
import matplotlib.pyplot as plt
from CoordGeo.plotting import annotate, plot_curve, plot_label, plot_line, plot_points

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# The written solution gives p = 3. With this value,
# 3x^2 - 6*sqrt(5)*x + 15 = 3(x - sqrt(5))^2.
# The curve therefore touches the x-axis once, at x = sqrt(5).
p = 3
root = np.sqrt(5)
x = np.linspace(-0.5, 5, 600)
y = p * (x - root) ** 2

fig, ax = plt.subplots(figsize=(6.5, 3.35))
plot_curve(ax, x, y, color="black", linewidth=1.8,
            label=r"$y=3x^2-6\sqrt{5}x+15$")
plot_line(ax, (-0.5, 0), (5, 0), color="0.35", linewidth=1.0)
plot_line(ax, (0, -2), (0, 48), color="0.35", linewidth=1.0)
plot_points(ax, [(root, 0)], color="black", zorder=4, s=26)
annotate(ax, r"Repeated root: $x=\sqrt{5}$", xy=(root, 0),
          xytext=(root + 0.55, 12),
          arrowprops={"arrowstyle": "->", "lw": 0.9}, fontsize=9)
plot_label(ax, 0.04, 24, r"$D=0$: the curve touches the $x$-axis once", fontsize=9)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(-0.5, 5)
ax.set_ylim(-2, 48)
ax.grid(True, alpha=0.22)
ax.legend(frameon=False, loc="upper right", fontsize=8)
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q01_Quadratic.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print("Q1: plotted the p=3 parabola with its repeated root at x=sqrt(5).")
