"""Draw the schematic chord-and-tangent figure for Q4."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from CoordGeo.plotting import plot_curve, plot_label, plot_line

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# Use a unit circle to keep the picture simple; the given angles are explained
# in the written solution, so this drawing is only a geometric illustration.
angles = np.linspace(0, 2 * np.pi, 500)
fig, ax = plt.subplots(figsize=(5.3, 3.7))
plot_curve(ax, np.cos(angles), np.sin(angles), linewidth=1.5)

P = np.array([0.0, -1.0])
Q = np.array([np.cos(np.pi / 6), np.sin(np.pi / 6)])
R = np.array([np.cos(-np.pi / 3), np.sin(-np.pi / 3)])
O = np.array([0.0, 0.0])
T = np.array([1.8, -1.0])

# Join the points to show the two chords, radii, and tangent at P.
segments = [(P, Q, "-"), (P, R, "-"), (Q, R, "-"),
            (O, P, "--"), (O, Q, "--"), (P, T, "-")]
for start, end, style in segments:
    plot_line(ax, start, end, linestyle=style, linewidth=1.25)

labels = [("O", O, -0.12, 0.10), ("P", P, -0.18, -0.12),
          ("Q", Q, 0.04, 0.05), ("R", R, 0.05, -0.05),
          ("T", T, 0.03, -0.05)]
for name, point, dx, dy in labels:
    plot_label(ax, point[0] + dx, point[1] + dy, name, fontsize=10)

plot_label(ax, 0.25, -0.72, r"$60^\circ$", fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-1.35, 2.0)
ax.set_ylim(-1.5, 1.45)
ax.axis("off")
fig.tight_layout()
fig.savefig(ROOT / "figs" / "TangentChord.png", dpi=180, bbox_inches="tight")
plt.close(fig)
