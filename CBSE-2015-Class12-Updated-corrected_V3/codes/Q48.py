"""Plot and verify the piecewise-linear static characteristic in C12-Q48."""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

def characteristic(x):
    x = np.asarray(x, dtype=float)
    return 1.0 + 2.0 * np.maximum(-x, 0.0) + 2.0 * np.maximum(x - 1.0, 0.0)

# Three linear operating regions: falling segment, zero-gain plateau, rising segment.
x_left = np.linspace(-1.0, 0.0, 120)
x_mid = np.linspace(0.0, 1.0, 120)
x_right = np.linspace(1.0, 2.0, 120)

fig, ax = plt.subplots(figsize=(6.5, 4.0))
ax.plot(x_left, characteristic(x_left), label=r"$-1<x<0$: slope $-2$")
ax.plot(x_mid, characteristic(x_mid), label=r"$0<x<1$: plateau, slope $0$")
ax.plot(x_right, characteristic(x_right), label=r"$1<x<2$: slope $+2$")
ax.scatter([0, 1], [1, 1], zorder=4)

ax.axvline(0, linestyle=":", linewidth=0.8)
ax.axvline(1, linestyle=":", linewidth=0.8)
ax.annotate(r"$\partial_C f(0)=[-2,0]$", (0, 1), xytext=(-0.92, 1.55),
            arrowprops={"arrowstyle": "->"}, fontsize=8)
ax.annotate(r"$\partial_C f(1)=[0,2]$", (1, 1), xytext=(0.98, 0.45),
            arrowprops={"arrowstyle": "->"}, fontsize=8)
ax.text(0.5, 1.08, "zero incremental gain", ha="center", fontsize=8)

ax.set_xlim(-1, 2)
ax.set_ylim(0.2, 3.3)
ax.set_xlabel("Input x")
ax.set_ylabel("Output f(x)")
ax.set_title(r"C12-Q48: piecewise-linear static characteristic ($L=2$)")
ax.grid(alpha=0.25)
ax.legend(fontsize=7, loc="upper center", ncol=1)
fig.tight_layout()

output = Path("figs") / "Q48_Differentiability.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output, dpi=180)
plt.close(fig)

# Numerical slope checks away from the switching points.
eps = 1e-6
left_slope_0 = (characteristic(0.0) - characteristic(-eps)) / eps
right_slope_0 = (characteristic(eps) - characteristic(0.0)) / eps
left_slope_1 = (characteristic(1.0) - characteristic(1.0-eps)) / eps
right_slope_1 = (characteristic(1.0+eps) - characteristic(1.0)) / eps
assert np.allclose([left_slope_0, right_slope_0, left_slope_1, right_slope_1], [-2, 0, 0, 2], atol=1e-8)

# A dense pairwise check supports the sharp global Lipschitz bound.
samples = np.linspace(-1, 2, 301)
values = characteristic(samples)
for i in range(0, len(samples), 5):
    slopes = np.abs(values[i+1:] - values[i]) / np.abs(samples[i+1:] - samples[i])
    assert np.all(slopes <= 2.0 + 1e-12)

print("C12-Q48 nonsmooth-characteristic verification: PASS")
print("One-sided slopes at 0: -2 and 0; at 1: 0 and 2; Lipschitz constant: 2")
