import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_dir_pt
from CoordGeo.plotting.funcs import label_pts

# Given points
A = np.array([0, -3]).reshape(-1, 1)
B = np.array([-5, 7]).reshape(-1, 1)
C = np.array([-4, 5]).reshape(-1, 1)

# Direction vector of line BC
m = C - B

# Generate the line using CoordGeo
x_BC = line_dir_pt(m, B, -2, 6)

# Plot the line
plt.figure(figsize=(8, 8))
plt.plot(x_BC[0, :], x_BC[1, :], label="Line BC")

# Plot and label the points
points = np.block([A, B, C])
plt.scatter(points[0, :], points[1, :])
label_pts(points, ["A (0,-3)", "B (-5,7)", "C (-4,5)"])

plt.xlabel("x")
plt.ylabel("y")
plt.title("Collinearity of Three Points")
plt.grid(True)
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")

plt.show()
