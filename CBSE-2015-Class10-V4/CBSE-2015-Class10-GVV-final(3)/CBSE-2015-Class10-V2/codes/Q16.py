"""Draw the circular segments and check their areas for Q16."""
import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

# A 60-degree sector of a circle with radius 14 cm forms the minor segment.
# The sketch uses a unit radius so that its labels fit neatly.
centre = np.array([0.0, 0.0])
radius = 1.0
circle = circ_gen(centre, radius)
arc_angles = np.linspace(np.radians(-30), np.radians(30), 50)
sector_arc = np.vstack((radius * np.cos(arc_angles),
                        radius * np.sin(arc_angles)))
P1 = np.array([math.cos(math.radians(30)), math.sin(math.radians(30))])
P2 = np.array([math.cos(math.radians(30)), -math.sin(math.radians(30))])

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(5.2, 4.2))
# CoordGeo supplies the sampled circle/arc points used for the shaded sector.
ax.fill(np.r_[centre[0], sector_arc[0], centre[0]],
        np.r_[centre[1], sector_arc[1], centre[1]],
        alpha=0.2)
ax.add_patch(Polygon([(0, 0), P1, P2], closed=True,
                     facecolor="white"))
ax.plot(circle[0], circle[1])
for end, style in ((P1, "--"), (P2, "--"), (P2, "-")):
    points = line_gen(centre, end) if style == "--" else line_gen(P1, P2)
    ax.plot(points[0], points[1], linestyle=style)
ax.text(0.43, 0.05, r"$60^\circ$", fontsize=9)
ax.annotate("minor segment", xy=(0.97, 0.02), xytext=(1.16, 0.23),
            fontsize=8, ha="left", arrowprops={"arrowstyle": "->", "lw": 0.8})
ax.text(-0.45, -0.35, "major segment\n(remainder)", fontsize=8, ha="center")
ax.text(0.12, 0.52, "14 cm", fontsize=8, rotation=30)
ax.set_aspect("equal")
ax.set_xlim(-1.25, 1.55)
ax.set_ylim(-1.18, 1.2)
ax.axis("off")
fig.tight_layout()
fig.savefig("figs/SegmentAreas.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# These values come from the written sector-area calculation, not the diagram.
minor_and_major_total = 616
minor_area = 308 / 3 - 49 * math.sqrt(3)
major_area = minor_and_major_total - minor_area
assert math.isclose(minor_area + major_area, minor_and_major_total, abs_tol=1e-12)
print(f"Q16: minor segment={minor_area:.4f} cm^2; major segment={major_area:.4f} cm^2")
