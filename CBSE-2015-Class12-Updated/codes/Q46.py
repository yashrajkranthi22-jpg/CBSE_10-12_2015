"""Plot the enclosed area for Q46 using CoordGeo's parabola and line generators."""
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.conics.funcs import parab_gen
from CoordGeo.line.funcs import line_gen

# Use a=1 only to make the diagram easy to read; the algebra shows m is scale-free.
a = 1.0
m = (4/3) ** (1/3)  # Value obtained in the written derivation.
x_intersection = a / m**2
y_intersection = 4*a / m

# CoordGeo defines x=y^2/c for y^2=c*x, so c=16a here.
y_curve = np.linspace(0, y_intersection, 300)
x_curve = parab_gen(y_curve, 16*a)
x_line_endpoints = line_gen(np.array([0.0, 0.0]), np.array([x_intersection, y_intersection]))
x_fill = np.linspace(0, x_intersection, 300)
y_parabola = 4*np.sqrt(a*x_fill)
y_line = 4*m*x_fill

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(6.5, 4.1))
ax.plot(x_curve, y_curve, label=r"$y^2=16ax$ (upper branch)")
ax.plot(x_line_endpoints[0], x_line_endpoints[1], label=r"$y=4mx$")
ax.fill_between(x_fill, y_line, y_parabola, alpha=0.23, label="bounded area")
ax.scatter([0, x_intersection], [0, y_intersection], zorder=4)
ax.annotate("intersection", (x_intersection, y_intersection), xytext=(x_intersection*0.58, y_intersection*1.04),
            arrowprops={"arrowstyle": "->"}, fontsize=8)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Q46: area between parabola and line ($a=1$ for display)")
ax.grid(alpha=0.25)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig("figs/Q46_ParabolaArea.png", dpi=180)
plt.close(fig)

area_from_formula = 2*a**2/(3*m**3)
print("area condition residual (should be 0):", area_from_formula - a**2/2)
print("theoretical m:", m)
