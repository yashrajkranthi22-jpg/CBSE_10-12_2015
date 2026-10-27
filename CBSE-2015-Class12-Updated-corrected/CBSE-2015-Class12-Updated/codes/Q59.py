"""Plot the Q59 feasible region, using CoordGeo to generate boundary lines."""
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen

# Theoretically derived intercepts for the three constraint boundaries.
boundaries = [
    (np.array([0.0, 5.0]), np.array([10.0, 0.0]), r"$x+2y=10$"),
    (np.array([0.0, 6.0]), np.array([6.0, 0.0]), r"$x+y=6$"),
    (np.array([0.0, 8.0]), np.array([8/3, 0.0]), r"$3x+y=8$"),
]
# The feasible region is unbounded; shade its visible portion within this window.
visible_region = np.array([[0, 8], [1, 5], [2, 4], [10, 0], [11, 0], [11, 10], [0, 10]], dtype=float)
# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(6.5, 4.2))
for start, end, label in boundaries:
    points = line_gen(start, end)
    ax.plot(points[0], points[1], label=label)
ax.fill(visible_region[:, 0], visible_region[:, 1], alpha=0.15,
        label="feasible region (visible window)")
ax.scatter([2], [4], zorder=4)
ax.annotate("minimum (2, 4), z = 26", (2, 4), xytext=(2.8, 2.6),
            arrowprops={"arrowstyle": "->"})
ax.set_xlim(0, 11)
ax.set_ylim(0, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Graphical solution: minimize z = 3x + 5y")
ax.grid(alpha=0.25)
ax.legend(fontsize=8, loc="upper right")
fig.tight_layout()
fig.savefig("figs/Q59_LPPMin.png", dpi=180)
plt.close(fig)

# Check only the already-derived minimum corner in the objective function.
print("objective at theoretical corner (2, 4):", 3*2 + 5*4, "(expected: 26)")
