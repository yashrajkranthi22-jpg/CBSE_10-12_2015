"""Plot the Q15 PMF using a stem plot."""

import numpy as np
import matplotlib.pyplot as plt

# Theoretical probabilities
categories = ["Red", "Blue", "Orange"]
probabilities = [1 / 4, 1 / 3, 5 / 12]
fractions = [r"$1/4$", r"$1/3$", r"$5/12$"]

# Discrete x-axis positions
x = np.arange(len(categories))

# Create the stem plot
fig, ax = plt.subplots(figsize=(5.7, 3.25))

markerline, stemlines, baseline = ax.stem(x, probabilities)

# Display exact fractions above the markers
for xi, probability, fraction in zip(x, probabilities, fractions):
    ax.annotate(fraction, (xi, probability),
                xytext=(0, 9), textcoords="offset points",
                ha="center", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(0, 0.49)
ax.set_ylabel("Probability")
ax.set_title("PMF of the ball colour", fontsize=10)
ax.grid(axis="y", alpha=0.22)

fig.tight_layout()
fig.savefig("figs/C10/Q15.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print("Q15: plotted the theoretical colour probabilities using a stem plot.")
