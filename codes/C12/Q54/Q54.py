import csv
import matplotlib.pyplot as plt

# Read the final experimental probability.
experimental_probability = None

with open("simulation.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        value = row["experimental_probability"]

        if value != "nan":
            experimental_probability = float(value)

if experimental_probability is None:
    raise ValueError("No valid experimental probability found.")

# Theoretical probability.
theoretical_probability = 8 / 11

# Create two stem plots on the same axes.
plt.figure(figsize=(8, 5))

experimental = plt.stem(
    [1],
    [experimental_probability],
    linefmt="C0-",
    markerfmt="C0o",
    basefmt=" "
)

theoretical = plt.stem(
    [2],
    [theoretical_probability],
    linefmt="C1-",
    markerfmt="C1s",
    basefmt=" "
)

experimental.markerline.set_label("Experimental Probability")
theoretical.markerline.set_label("Theoretical Probability")

# Axis formatting.
plt.xticks([1, 2], ["Experimental", "Theoretical"])
plt.xlabel("Type of Probability")
plt.ylabel("Probability")

plt.title("Experimental vs Theoretical Probability")

plt.ylim(0, 1)
plt.grid(True, axis="y")
plt.legend()
plt.tight_layout()

plt.savefig("probability_comparison.png", dpi=300)
plt.close()
