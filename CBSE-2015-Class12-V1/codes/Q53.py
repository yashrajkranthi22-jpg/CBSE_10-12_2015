"""Plot the theoretical PMF for the five-step random walk in Question 53."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
# Theoretical binomial probabilities for k = 0, ..., 5 forward steps.
# Net displacement is 2k - 5, so the outcome labels are -5, -3, -1, 1, 3, 5.
displacement = [-5, -3, -1, 1, 3, 5]
probabilities = [0.07776, 0.2592, 0.3456, 0.2304, 0.0768, 0.01024]

fig, ax = plt.subplots(figsize=(6.6, 3.8))
ax.bar(displacement, probabilities, width=0.7)
ax.set_xlabel("Net displacement (steps)")
ax.set_ylabel("Probability")
ax.set_title("Five-step random walk: theoretical PMF")
ax.set_xticks(displacement)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q53_WalkPMF.png", dpi=180)
plt.close(fig)

# A position one step from the start is displacement -1 or +1.
required_probability = 0.3456 + 0.2304
print("P(one step away):", required_probability, "(theoretical value: 0.576)")
print("PMF total:", sum(probabilities), "(required: 1)")
