import matplotlib.pyplot as plt
from collections import Counter

# Read the generated dice outcomes
generated_products = []

with open("dice_data.dat", "r") as file:
    for line in file:
        if not line.strip():
            continue

        values = list(map(int, line.split()))

        if len(values) < 3:
            raise ValueError("Invalid data in dice_data.dat")

        die1, die2, product = values[:3]

        if not (1 <= die1 <= 6 and 1 <= die2 <= 6):
            raise ValueError("Invalid dice outcome")

        if product != die1 * die2:
            raise ValueError("Incorrect product in data file")

        generated_products.append(product)

total_rolls = len(generated_products)

if total_rolls == 0:
    raise ValueError("No dice outcomes found in dice_data.dat")


# Consider every integer from 1 to 36
products = list(range(1, 37))


# Calculate experimental probabilities
experimental_counts = Counter(generated_products)

experimental_probabilities = [
    experimental_counts[x] / total_rolls
    for x in products
]


# Calculate theoretical probabilities
theoretical_counts = {x: 0 for x in products}

for die1 in range(1, 7):
    for die2 in range(1, 7):
        theoretical_counts[die1 * die2] += 1

theoretical_probabilities = [
    theoretical_counts[x] / 36
    for x in products
]


# Plot both PMFs on the same axes
fig, ax = plt.subplots(figsize=(13, 6))

ax.stem(
    products,
    experimental_probabilities,
    linefmt="-",
    markerfmt="o",
    basefmt=" ",
    label="Experimental PMF"
)

ax.stem(
    products,
    theoretical_probabilities,
    linefmt="--",
    markerfmt="x",
    basefmt=" ",
    label="Theoretical PMF"
)

ax.set_title("Experimental vs Theoretical PMF of the Product of Two Dice")
ax.set_xlabel("Product of the two dice")
ax.set_ylabel("Probability")

ax.set_xticks(products)
ax.set_xlim(0, 37)
ax.set_ylim(bottom=0)

ax.grid(axis="y", alpha=0.25)
ax.legend()

fig.tight_layout()

fig.savefig(
    "dice_pmf_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Plot saved as dice_pmf_comparison.png")
