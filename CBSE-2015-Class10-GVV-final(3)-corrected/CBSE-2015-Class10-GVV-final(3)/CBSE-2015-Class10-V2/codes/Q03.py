"""Plot the product-dice PMF using outcome counts worked out on paper."""

import matplotlib.pyplot as plt


# From the 6-by-6 outcome table, count the ordered pairs giving each product.
# For example, product 4 has (1,4), (2,2), (4,1), while product 6 has
# (1,6), (2,3), (3,2), (6,1). These theoretical counts add up to 36.
products = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36]
favourable_counts = [1, 2, 2, 3, 2, 4, 2, 1, 2, 4, 2, 1, 2, 2, 2, 1, 2, 1]

# All 36 ordered outcomes are equally likely, so P(product=x) = count(x)/36.
probabilities = [count / 36 for count in favourable_counts]
positions = range(len(products))

# Keep the plotting setup separate so the labels and limits are easy to adjust.
fig, ax = plt.subplots(figsize=(7.2, 3.35))
ax.bar(positions, probabilities)
ax.set_xticks(list(positions), [str(value) for value in products], fontsize=7.5)
ax.set_xlabel("Product of the two dice")
ax.set_ylabel("Probability")
ax.set_title("PMF of the product of two fair dice", fontsize=10)
ax.grid(axis="y", alpha=0.22)
ax.set_ylim(0, max(probabilities) * 1.28)
ax.annotate(r"$P(X=6)=4/36=1/9$",
            xy=(products.index(6), probabilities[products.index(6)]),
            xytext=(products.index(6) + 2.5, max(probabilities) * 1.13),
            arrowprops={"arrowstyle": "->", "lw": 0.9}, fontsize=8)
fig.tight_layout()
fig.savefig("figs/Q03_ProductPMF.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print("Q3: plotted the PMF from theoretical favourable-outcome counts divided by 36.")
