"""Draw the section-formula figure for Q14 using CoordGeo's line functions."""
# Keep the numerical check tied to the values established in the solution.
import matplotlib.pyplot as plt
import numpy as np

from CoordGeo.line.funcs import dir_vec, line_gen

# P divides AB internally in the ratio 3:4, so it is 3/7 of the way from A to B.
A = np.array([-2.0, -2.0])
B = np.array([2.0, -4.0])
P = A + (3 / 7) * dir_vec(A, B)

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(6, 3.8))
segment = line_gen(A, B)
ax.plot(segment[0], segment[1])
ax.scatter([A[0], P[0], B[0]], [A[1], P[1], B[1]], s=28, zorder=3)
for name, point, dx, dy in [
    ("A", A, -0.2, 0.18), ("P", P, 0.05, 0.16), ("B", B, 0.06, -0.2)
]:
    shown_point = tuple(int(value) if float(value).is_integer() else float(value) for value in point)
    label = f"{name} {shown_point}" if name != "P" else name
    ax.text(point[0] + dx, point[1] + dy, label, fontsize=9)
ax.text((A[0] + P[0]) / 2, (A[1] + P[1]) / 2 + 0.12,
        "3 parts", ha="center", fontsize=9)
ax.text((P[0] + B[0]) / 2, (P[1] + B[1]) / 2 - 0.25,
        "4 parts", ha="center", fontsize=9)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True, alpha=0.25)
ax.set_xlim(-2.6, 2.7)
ax.set_ylim(-4.8, -1.3)
fig.tight_layout()
fig.savefig("figs/SectionPoint.png", dpi=180, bbox_inches="tight")
plt.close(fig)
