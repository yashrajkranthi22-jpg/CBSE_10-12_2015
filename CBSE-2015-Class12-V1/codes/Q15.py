"""Plot the line-plane intersection and verify the theoretical point for Question 15."""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codes" / "CoordGeo"))
from line.funcs import line_gen, line_dir_pt

A = np.array([3.0, 4.0, 1.0])
B = np.array([5.0, 1.0, 6.0])
P = np.array([2.0, 1.0, 2.0])
Q = np.array([3.0, 1.0, 0.0])
R = np.array([4.0, -2.0, 1.0])
# The written solution derives this intersection, and the script only checks it.
I = np.array([5/3, 6.0, -7/3])

# The given plane has equation 2x + y + z = 7, so z can be plotted directly.
x = np.linspace(0.5, 4.8, 28)
y = np.linspace(-2.5, 7.0, 34)
X, Y = np.meshgrid(x, y)
Z = 7 - 2*X - Y
line_points = line_dir_pt(B - A, A, -0.9, 1.1)

fig = plt.figure(figsize=(7.1, 5.3))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, alpha=0.22, linewidth=0)
for start, end, name in [(P, Q, "PQ"), (Q, R, "QR"), (R, P, "RP")]:
    points = line_gen(start, end)
    ax.plot(points[0], points[1], points[2], linewidth=2, label=name)
ax.plot(line_points[0], line_points[1], line_points[2], linewidth=2, label="line AB (extended)")
ax.scatter(*A, label="A")
ax.scatter(*B, label="B")
ax.scatter(*I, s=55, label="intersection I")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Q15: intersection of line AB with plane PQR")
ax.legend(fontsize=7, loc="upper left")
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q15_3D.png", dpi=180)
plt.close(fig)

line_residual = np.linalg.norm(I - (A + (-2/3)*(B-A)))
plane_residual = 2*I[0] + I[1] + I[2] - 7
print("line residual (should be 0):", line_residual)
print("plane residual (should be 0):", plane_residual)
