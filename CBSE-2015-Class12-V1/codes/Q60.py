"""Plot the Q60 machine-purchase region using CoordGeo boundary-line points."""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codes" / "CoordGeo"))
from line.funcs import line_gen

# Intercepts come from the two constraint equations already solved in the text.
budget_line = line_gen(np.array([0.0, 24.0]), np.array([16.0, 0.0]))
space_line = line_gen(np.array([0.0, 20.0]), np.array([20.0, 0.0]))
vertices = np.array([[0, 0], [16, 0], [8, 12], [0, 20]], dtype=float)

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.fill(vertices[:, 0], vertices[:, 1], alpha=0.18, label="feasible purchases")
ax.plot(budget_line[0], budget_line[1], label=r"$3x+2y=48$ (budget)")
ax.plot(space_line[0], space_line[1], label=r"$x+y=20$ (space)")
ax.scatter([8], [12], zorder=4)
ax.annotate("(8, 12): Rs. 3920", (8, 12), xytext=(9, 14),
            arrowprops={"arrowstyle": "->"})
ax.set_xlim(0, 21)
ax.set_ylim(0, 25)
ax.set_xlabel("Electronic machines, x")
ax.set_ylabel("Manual machines, y")
ax.set_title("Machine-purchase LPP")
ax.grid(alpha=0.25)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q60_LPPProfit.png", dpi=180)
plt.close(fig)

# Verify profits at the theoretically identified feasible corners.
profits = [(0, 0, 0), (16, 0, 220*16), (8, 12, 220*8 + 180*12), (0, 20, 180*20)]
print("corner profits (x, y, rupees):", profits)
