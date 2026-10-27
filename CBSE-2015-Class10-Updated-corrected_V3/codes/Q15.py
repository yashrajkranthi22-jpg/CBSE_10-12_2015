"""Plot the Q15 PMF from the probabilities derived in the written solution."""

import matplotlib.pyplot as plt


# Theoretical probabilities: red = 1/4, blue = 1/3, and orange = 5/12.
# The orange probability is the remainder 1 - 1/4 - 1/3 = 5/12.
categories = ["Red", "Blue", "Orange"]
# These values come from the cases counted in the written solution.
probabilities = [1 / 4, 1 / 3, 5 / 12]
fractions = [r"$1/4$", r"$1/3$", r"$5/12$"]

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(5.7, 3.25))
bars = ax.bar(categories, probabilities)

# Print the exact fractions above the bars rather than rounded decimals.
for bar, fraction in zip(bars, fractions):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.012,
            fraction, ha="center", va="bottom", fontsize=10)

ax.set_ylim(0, 0.49)
ax.set_ylabel("Probability")
ax.set_title("PMF of the ball colour", fontsize=10)
ax.grid(axis="y", alpha=0.22)
fig.tight_layout()
fig.savefig("figs/Q15_ColourPMF.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print("Q15: plotted the theoretically calculated colour probabilities.")
