"""Check the aeroplane speed in Q13 and draw the position diagram."""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import plot_label, plot_line, plot_points


ROOT = Path(__file__).resolve().parents[1]

# The plane stays at height h. For a ground angle theta, tan(theta) = h / x.
height = 1500 * math.sqrt(3)
x_at_60 = height / math.tan(math.radians(60))
x_at_30 = height / math.tan(math.radians(30))

# Horizontal distance divided by time gives m/s; multiply by 3.6 to get km/h.
time_seconds = 15
speed_kmh = (x_at_30 - x_at_60) / time_seconds * 3.6
assert math.isclose(x_at_60, 1500, abs_tol=1e-9)
assert math.isclose(x_at_30, 4500, abs_tol=1e-9)
assert math.isclose(speed_kmh, 720, abs_tol=1e-9)

A = (0, 0)
P1 = (x_at_60, height)
P2 = (x_at_30, height)
fig, ax = plt.subplots(figsize=(7, 3.3))
plot_line(ax, A, P1, linewidth=1.8)
plot_line(ax, A, P2, linewidth=1.8, linestyle="--")
plot_line(ax, P1, P2, linewidth=2.2)
plot_line(ax, (P1[0], 0), P1, linestyle=":", linewidth=1.2)
plot_line(ax, (P2[0], 0), P2, linestyle=":", linewidth=1.2)
plot_points(ax, [A, P1, P2], s=22, zorder=3)
plot_label(ax, -120, -130, "A", fontsize=10)
plot_label(ax, x_at_60, height + 110, "60°", ha="center", fontsize=10)
plot_label(ax, x_at_30, height + 110, "30°", ha="center", fontsize=10)
plot_label(ax, (x_at_60 + x_at_30) / 2, height + 260,
         "3000 m in 15 s", ha="center", fontsize=9)
plot_label(ax, x_at_30 + 90, height / 2, r"$1500\sqrt{3}$ m",
         rotation=90, va="center", fontsize=9)
ax.set_xlim(-250, x_at_30 + 500)
ax.set_ylim(-250, height + 520)
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Aeroplane.png", dpi=180, bbox_inches="tight")
plt.close(fig)
print(f"Q13: x1={x_at_60:.0f} m, x2={x_at_30:.0f} m, speed={speed_kmh:.0f} km/h")
