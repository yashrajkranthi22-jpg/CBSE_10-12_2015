"""Generate the product PMF from the discrete push-forward map (i,j) -> i*j."""
from collections import Counter
from itertools import product

import matplotlib.pyplot as plt

outcomes = list(product(range(1, 7), repeat=2))
counts = Counter(i * j for i, j in outcomes)
assert len(outcomes) == 36
assert sum(counts.values()) == 36
assert counts[6] == 4

products = sorted(counts)
probabilities = [counts[m] / 36 for m in products]
pgf_coefficients = {m: counts[m] / 36 for m in products}
assert abs(sum(pgf_coefficients.values()) - 1.0) < 1e-12
assert pgf_coefficients[6] == 1 / 9

fig, ax = plt.subplots(figsize=(7.2, 3.35))
ax.bar(range(len(products)), probabilities)
ax.set_xticks(range(len(products)), [str(m) for m in products], fontsize=7.5)
ax.set_xlabel("Product random variable Z = X Y")
ax.set_ylabel("Probability P(Z = m)")
ax.set_title("Push-forward PMF of the product of two fair dice", fontsize=10)
ax.grid(axis="y", alpha=0.22)
ax.set_ylim(0, max(probabilities) * 1.28)
ax.annotate(r"$[w^6]G_Z(w)=4/36=1/9$",
            xy=(products.index(6), probabilities[products.index(6)]),
            xytext=(products.index(6) + 2.5, max(probabilities) * 1.13),
            arrowprops={"arrowstyle": "->", "lw": 0.9}, fontsize=8)
fig.tight_layout()
fig.savefig("figs/Q03_ProductPMF.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print("C10-Q03 push-forward PMF/PGF verification: PASS")
print("G_Z(1) =", sum(pgf_coefficients.values()), "; P(Z=6) =", pgf_coefficients[6])
