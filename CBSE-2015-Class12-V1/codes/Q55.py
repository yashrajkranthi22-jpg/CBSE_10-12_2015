"""Plot the theoretical PMF for the number of black balls in Question 55."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
# Choose 2 balls from 7, of which 2 are black and 5 red.
x_values = [0, 1, 2]
probabilities = [10/21, 10/21, 1/21]

fig, ax = plt.subplots(figsize=(6.2, 3.7))
ax.bar(x_values, probabilities, width=0.55)
ax.set_xticks(x_values)
ax.set_xlabel("Number of black balls, X")
ax.set_ylabel("P(X = x)")
ax.set_title("Theoretical PMF for two draws without replacement")
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(ROOT / "figs" / "Q55_BlackBallsPMF.png", dpi=180)
plt.close(fig)

mean = sum(x*p for x, p in zip(x_values, probabilities))
second_moment = sum(x*x*p for x, p in zip(x_values, probabilities))
variance = second_moment - mean**2
print("probabilities sum to:", sum(probabilities))
print("mean:", mean, "(theoretical value: 4/7)")
print("variance:", variance, "(theoretical value: 50/147)")
