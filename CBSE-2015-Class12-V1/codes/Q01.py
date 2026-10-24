"""Plot and check the theoretically derived vector for Question 1."""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
# CoordGeo's line generator also accepts 3D endpoint vectors. It supplies the
# points for each arrow; Matplotlib's 3D axes draw them.
sys.path.insert(0, str(ROOT / "codes" / "CoordGeo"))
from line.funcs import line_gen

a = np.array([1.0, -2.0, -3.0])
b = np.array([3.0, -1.0, -2.0])
# This is the answer already derived in the written solution; the script checks it.
d = (np.sqrt(57) / 5) * np.array([1.0, -7.0, 5.0])
origin = np.zeros(3)

fig = plt.figure(figsize=(7.0, 5.2))
ax = fig.add_subplot(111, projection="3d")
# The finite parallelogram helps show the plane spanned by a and b.
u, v = np.meshgrid(np.linspace(0, 1, 12), np.linspace(0, 1, 12))
plane_points = u[..., None] * a + v[..., None] * b
ax.plot_surface(plane_points[:, :, 0], plane_points[:, :, 1], plane_points[:, :, 2], alpha=0.22)
for vector, label in [(a, r"$a$"), (b, r"$b$"), (d, r"$d$ (answer)")]:
    points = line_gen(origin, vector)
    ax.plot(points[0], points[1], points[2], linewidth=2, label=label)
    ax.quiver(0, 0, 0, *vector, arrow_length_ratio=0.08)
    ax.text(*vector, label)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Q1: the answer vector is normal to the plane spanned by a and b")
ax.legend(fontsize=8)
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q01_3D.png", dpi=180)
plt.close(fig)

print("a dot d (should be 0):", np.dot(a, d))
print("b dot d (should be 0):", np.dot(b, d))
print("magnitude (should be sqrt(171)):", np.linalg.norm(d), "required:", np.sqrt(171))
