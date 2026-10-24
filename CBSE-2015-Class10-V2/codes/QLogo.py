"""Draw the decorative bridge emblem used on the cover."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
fig, ax = plt.subplots(figsize=(4.0, 3.0))

# A simple downward parabola stands in for the bridge's main cable.
x = np.linspace(-3, 3, 400)
y = 1.55 - 0.275 * x**2
ax.plot([-3, 3], [-1, -1], color="#e6b51d", linewidth=5.0, solid_capstyle="round")
ax.plot(x[x <= 0], y[x <= 0], color="#1684d9", linewidth=5.5, solid_capstyle="round")
ax.plot(x[x >= 0], y[x >= 0], color="#78513f", linewidth=5.5, solid_capstyle="round")
ax.plot([0, 0], [-1, 1.62], color="#d7a078", linewidth=5.0, solid_capstyle="round")

# Thin vertical lines connect the deck to the two halves of the cable.
for cable_x in np.linspace(-2.8, -0.12, 14):
    cable_y = 1.55 - 0.275 * cable_x**2
    ax.plot([cable_x, cable_x], [-1, cable_y], color="#b74f4c", linewidth=0.8, alpha=0.96)
for cable_x in np.linspace(0.12, 2.8, 14):
    cable_y = 1.55 - 0.275 * cable_x**2
    ax.plot([cable_x, cable_x], [-1, cable_y], color="#679a70", linewidth=0.8, alpha=0.96)

ax.set_xlim(-3.08, 3.08)
ax.set_ylim(-1.12, 1.78)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout(pad=0)
fig.savefig(ROOT / "figs" / "logo.jpg", dpi=240, bbox_inches="tight", facecolor="white")
plt.close(fig)
