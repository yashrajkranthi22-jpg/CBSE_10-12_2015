"""Show the shortest connector between the two parallel lines in Q6."""
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_dir_pt, line_gen

# Enter the coefficients from the equations derived above.
A = np.array([1.0, 2.0, 3.0])
B = np.array([2.0, 4.0, 5.0])
v = np.array([2.0, 3.0, 4.0])
# This foot was derived using perpendicular projection onto the first line.
foot = np.array([61/29, 106/29, 151/29], dtype=float)
answer_distance = np.sqrt(5/29)

# Plot short portions around the closest points rather than long lines; this
# zoom makes the shortest connector visible without changing the geometry.
line1 = line_dir_pt(v, A, 0.25, 0.85)
line2 = line_dir_pt(2*v, B, -0.18, 0.18)
perpendicular = line_gen(foot, B)

fig = plt.figure(figsize=(7.0, 5.2))
ax = fig.add_subplot(111, projection="3d")
ax.plot(line1[0], line1[1], line1[2],
        label=r"$L_1: (1,2,3)+\lambda(2,3,4)$")
ax.plot(line2[0], line2[1], line2[2],
        label=r"$L_2: (2,4,5)+\mu(4,6,8)$")
ax.plot(perpendicular[0], perpendicular[1], perpendicular[2], "--",
        label=r"shortest connector, $d=\sqrt{5/29}$")
ax.scatter(*B, s=45, label="point B on $L_2$")
ax.scatter(*foot, s=45, label="perpendicular foot on $L_1$")
ax.set_xlim(0.5, 3.5)
ax.set_ylim(2.5, 5.5)
ax.set_zlim(3.5, 6.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(elev=15, azim=30)
ax.set_title("Q6: zoomed view of the shortest distance")
ax.legend(fontsize=6.7, loc="upper left")
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
fig.savefig("figs/Q06_3D.png", dpi=180)
plt.close(fig)

# Substitute the theoretical foot into the line and perpendicularity conditions.
actual_distance = np.linalg.norm(B - foot)
print("foot lies on L1 (cross-product residual):", np.linalg.norm(np.cross(foot - A, v)))
print("connector perpendicular to direction (dot product):", np.dot(B - foot, v))
print("distance residual (expected 0):", actual_distance - answer_distance)
