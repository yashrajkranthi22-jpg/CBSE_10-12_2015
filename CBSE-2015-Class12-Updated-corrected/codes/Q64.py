"""Draw Q64 with CoordGeo's circle and line generators."""
# Keep the numerical check tied to the values established in the solution.
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

# Use the angle/value obtained in the written solution.
theta = np.pi / 4  # The theoretically optimal tangent point is at 45 degrees.
px, py = 2*np.cos(theta), 2*np.sin(theta)
intercept = 2/np.cos(theta)
circle = circ_gen(np.array([0.0, 0.0]).reshape(-1, 1), 2.0)
tangent = line_gen(np.array([intercept, 0.0]), np.array([0.0, intercept]))

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(5.8, 5.0))
ax.plot(circle[0], circle[1], label=r"$x^2+y^2=4$")
ax.plot(tangent[0], tangent[1], label="tangent at 45 degrees")
ax.scatter([px], [py], zorder=4)
ax.plot([px, intercept], [py, 0], linestyle="--")
ax.plot([px, 0], [py, intercept], linestyle="--")
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 3.5)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Minimum $OA+OB=4\sqrt{2}$")
ax.grid(alpha=0.25)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig("figs/Q64_CircleTangent.png", dpi=180)
plt.close(fig)

print("equal intercepts:", intercept, intercept)
print("minimum sum:", 2*intercept, "(theoretical value: 4 sqrt(2))")
