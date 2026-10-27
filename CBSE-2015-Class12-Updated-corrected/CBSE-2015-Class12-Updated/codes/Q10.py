"""Plot Q10's planes with a legend identifying each plane."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

from CoordGeo.line.funcs import line_gen, line_dir_pt

# The plane equation and direction below are obtained in the written solution.
final_normal = np.array([109.0, 27.0, -22.0])
final_constant = -81.0
line_direction = np.array([2.0, -4.0, 5.0])
intersection_point = np.array([0.0, 3.0, 0.0])

x = np.linspace(-1.0, 2.4, 28)
y = np.linspace(-0.5, 5.5, 28)
X, Y = np.meshgrid(x, y)
Z1 = 2*X + Y - 3
Z2 = (-9 - 5*X + 3*Y) / 4
Z3 = (109*X + 27*Y - 81) / 22

shared_line = line_dir_pt(np.array([1.0, -13.0, -11.0]), intersection_point, -0.32, 0.32)
parallel_line = line_gen(-0.5*line_direction, 0.5*line_direction)

fig = plt.figure(figsize=(7.3, 5.5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z1, alpha=0.28)
ax.plot_surface(X, Y, Z2, alpha=0.28)
ax.plot_surface(X, Y, Z3, alpha=0.30)
ax.plot(shared_line[0], shared_line[1], shared_line[2])
ax.plot(parallel_line[0], parallel_line[1], parallel_line[2], linestyle="--")
ax.scatter(*intersection_point, s=28)

# Proxy legend entries make the surface equations unambiguous.
legend_handles = [
    Patch(alpha=0.45, label=r"given plane $2x+y-z=3$"),
    Patch(alpha=0.45, label=r"given plane $5x-3y+4z+9=0$"),
    Patch(alpha=0.45, label=r"required plane $109x+27y-22z-81=0$"),
    Line2D([0], [0], label="intersection line of the given planes"),
    Line2D([0], [0], ls="--", label="given line direction"),
    Line2D([0], [0], marker="o", label="point: (0, 3, 0)"),
]
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Q10: plane through the intersection and parallel to the line")
ax.view_init(elev=22, azim=-58)
ax.legend(handles=legend_handles, fontsize=6.1, loc="upper left")
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
fig.savefig("figs/Q10_3D.png", dpi=180)
plt.close(fig)

# These checks only substitute the theoretical plane into the conditions.
P1 = np.array([2.0, 1.0, -1.0, -3.0])
P2 = np.array([5.0, -3.0, 4.0, 9.0])
print("normal dot line direction (expected 0):", np.dot(final_normal, line_direction))
print("plane-combination residual:", np.array([109, 27, -22, -81]) - (42*P1 + 5*P2))
print("common point residual (expected 0):", final_normal @ intersection_point + final_constant)
