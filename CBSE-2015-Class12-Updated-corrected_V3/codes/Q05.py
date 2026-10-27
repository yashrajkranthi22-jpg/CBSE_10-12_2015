"""Plot the Q5 vectors used in the written solution."""
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen

a = np.array([1.0, 4.0, 2.0])
b = np.array([3.0, -2.0, 7.0])
c = np.array([2.0, -1.0, 4.0])
# The theoretical solution is d = (96, -3, -42). Show scaled directions so
# all four vectors remain visible on a single set of axes.
d = np.array([96.0, -3.0, -42.0])
origin = np.zeros(3)
vectors = [
    (a, r"$a=(1,4,2)$"),
    (b, r"$b=(3,-2,7)$"),
    (c, r"$c=(2,-1,4)$"),
    (d, r"$d=(96,-3,-42)$"),
]

fig = plt.figure(figsize=(7.0, 5.2))
ax = fig.add_subplot(111, projection="3d")
for vector, label in vectors:
    direction = vector / np.linalg.norm(vector)
    endpoint = 3 * direction
    points = line_gen(origin, endpoint)
    ax.plot(points[0], points[1], points[2], label=label)
    ax.quiver(*origin, *endpoint, arrow_length_ratio=0.10)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Q5: vector directions (normalised for readability)")
ax.legend(fontsize=7, loc="upper left")
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
fig.savefig("figs/Q05_3D.png", dpi=180)
plt.close(fig)

# These checks only substitute the already-derived vector into the conditions.
print("a dot d (expected 0):", np.dot(a, d))
print("b dot d (expected 0):", np.dot(b, d))
print("c dot d (expected 27):", np.dot(c, d))
