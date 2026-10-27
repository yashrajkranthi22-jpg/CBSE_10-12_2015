"""Plot Q52's piecewise function to show it has no jump discontinuity."""
import numpy as np
import matplotlib.pyplot as plt


# On [-1, 0], x(1-x) <= 0, so f(x) = 2x - x^2.
left_x = np.linspace(-1, 0, 250)
left_y = 2*left_x - left_x**2
# On [0, 1], x(1-x) >= 0, so f(x) = x^2.
right_x = np.linspace(0, 1, 250)
right_y = right_x**2

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(6.4, 3.7))
ax.plot(left_x, left_y, label=r"$2x-x^2$, $-1\leq x\leq0$")
ax.plot(right_x, right_y, label=r"$x^2$, $0\leq x\leq1$")
# The branches meet at (0, 0), so there is no jump at the joining point.
ax.scatter([0], [0], s=35, zorder=4, label="common value f(0) = 0")
ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-3.2, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Q52: both pieces meet continuously at x = 0")
ax.grid(alpha=0.25)
ax.legend(fontsize=7.1, loc="lower right")
fig.tight_layout()
fig.savefig("figs/Q52_Continuity.png", dpi=180)
plt.close(fig)

print("left-hand limit at 0:", 2*0 - 0**2)
print("right-hand limit at 0:", 0**2)
print("function value at 0:", 0 - abs(0 - 0**2))
