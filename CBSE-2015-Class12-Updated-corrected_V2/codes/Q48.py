"""Plot one-sided slopes for the continuity/differentiability question Q48."""
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen

# CoordGeo generates each straight segment of the piecewise-linear function.
segments = [
    (np.array([-1.0, 3.0]), np.array([0.0, 1.0]), r"$f(x)=1-2x$, slope $-2$"),
    (np.array([0.0, 1.0]), np.array([1.0, 1.0]), r"$f(x)=1$, slope $0$"),
    (np.array([1.0, 1.0]), np.array([2.0, 3.0]), r"$f(x)=2x-1$, slope $2$"),
]
# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(6.5, 4.0))
for start, end, label in segments:
    points = line_gen(start, end)
    ax.plot(points[0], points[1], label=label)

# Draw short tangent/one-sided slope segments near both corners.
slopes = [
    (np.array([-0.5, 2.0]), np.array([0.0, 1.0]), "left slope -2 at 0"),
    (np.array([0.0, 1.0]), np.array([0.5, 1.0]), "right slope 0 at 0"),
    (np.array([0.5, 1.0]), np.array([1.0, 1.0]), "left slope 0 at 1"),
    (np.array([1.0, 1.0]), np.array([1.5, 2.0]), "right slope 2 at 1"),
]
for start, end, label in slopes:
    points = line_gen(start, end)
    ax.plot(points[0], points[1], "--", label="_nolegend_")
ax.scatter([0, 1], [1, 1], zorder=4)
ax.annotate(r"slopes $-2$ and $0$", (0, 1), xytext=(-0.85, 1.45), arrowprops={"arrowstyle": "->"}, fontsize=8)
ax.annotate(r"slopes $0$ and $2$", (1, 1), xytext=(1.1, 0.55), arrowprops={"arrowstyle": "->"}, fontsize=8)
ax.set_xlim(-1, 2)
ax.set_ylim(0.25, 3.25)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Q48: continuous graph with unequal one-sided slopes at 0 and 1")
ax.grid(alpha=0.25)
ax.legend(fontsize=6.5, ncol=2, loc="upper center")
fig.tight_layout()
fig.savefig("figs/Q48_Differentiability.png", dpi=180)
plt.close(fig)

print("at x=0: left slope -2, right slope 0 -> not differentiable")
print("at x=1: left slope 0, right slope 2 -> not differentiable")
