"""Draw Q65 using CoordGeo's ellipse and line generators."""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codes" / "CoordGeo"))
from conics.funcs import ellipse_gen
from line.funcs import line_gen

ellipse = ellipse_gen(4.0, 3.0)
# Differentiation in the written solution gives u=-2 and v=3 sqrt(3) / 2.
u = -2.0
y = 3*np.sqrt(3)/2
vertices = [np.array([4.0, 0.0]), np.array([u, y]), np.array([u, -y])]

fig, ax = plt.subplots(figsize=(6.0, 4.8))
ax.plot(ellipse[0], ellipse[1], label=r"$x^2/16+y^2/9=1$")
for start, end in zip(vertices, vertices[1:] + vertices[:1]):
    side = line_gen(start, end)
    ax.plot(side[0], side[1], linewidth=1.5)
ax.scatter([v[0] for v in vertices], [v[1] for v in vertices], zorder=4)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Maximum area $9\sqrt{3}$")
ax.grid(alpha=0.25)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q65_EllipseTriangle.png", dpi=180)
plt.close(fig)

print("theoretical vertices:", vertices)
print("ellipse residual at base point:", u**2/16 + y**2/9 - 1)
print("area residual:", (4-u)*y - 9*np.sqrt(3), "(should be 0)")
