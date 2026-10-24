"""Plot the Q15 PMF from the probabilities derived in the written solution."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

# Theoretical probabilities: red = 1/4, blue = 1/3, and orange = 5/12.
# The orange probability is the remainder 1 - 1/4 - 1/3 = 5/12.
colours = ["Red", "Blue", "Orange"]
probabilities = [1 / 4, 1 / 3, 5 / 12]
fractions = [r"$1/4$", r"$1/3$", r"$5/12$"]

fig, ax = plt.subplots(figsize=(5.7, 3.25))
bars = ax.bar(colours, probabilities,
              color=["#d95f5f", "#4c78a8", "#f2a541"],
              edgecolor="black", linewidth=0.55)

# Print the exact fractions above the bars rather than rounded decimals.
for bar, fraction in zip(bars, fractions):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.012,
            fraction, ha="center", va="bottom", fontsize=10)

ax.set_ylim(0, 0.49)
ax.set_ylabel("Probability")
ax.set_title("PMF of the ball colour", fontsize=10)
ax.grid(axis="y", alpha=0.22)
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q15_ColourPMF.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print("Q15: plotted the theoretically calculated colour probabilities.")
