"""Plot and shade the circular segment in Q47 with CoordGeo geometry generators."""
# Keep the numerical check tied to the values established in the solution.
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

circle = circ_gen(np.array([0.0, 0.0]), 2.0)
chord = line_gen(np.array([0.0, 2.0]), np.array([2.0, 0.0]))
x = np.linspace(0, 2, 300)
y_circle = np.sqrt(4 - x**2)
y_chord = 2 - x

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(5.9, 5.0))
ax.plot(circle[0], circle[1], label=r"$x^2+y^2=4$")
ax.plot(chord[0], chord[1], label=r"$x+y=2$")
ax.fill_between(x, y_chord, y_circle, alpha=0.25, label=r"required region ($x+y\geq2$)")
ax.scatter([0, 2], [2, 0], zorder=4)
ax.set_xlim(-0.15, 2.25)
ax.set_ylim(-0.15, 2.25)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Q47: area inside the circle and above the chord")
ax.grid(alpha=0.25)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig("figs/Q47_CircleSegment.png", dpi=180)
plt.close(fig)

print("theoretical area:", np.pi - 2)
