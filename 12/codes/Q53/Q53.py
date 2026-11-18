import numpy as np
import matplotlib.pyplot as plt

# Read the experimental outcomes.
outcomes = np.loadtxt("random_walk.dat", dtype=int)

# Possible net displacements after five steps.
displacement = np.array([-5, -3, -1, 1, 3, 5])

# Calculate the practical PMF.
counts = np.array([np.sum(outcomes == x) for x in displacement])
practical_pmf = counts / len(outcomes)

# Theoretical PMF for five independent steps.
theoretical_pmf = np.array([1, 5, 10, 10, 5, 1]) / 32

# Plot both PMFs using stem plots.
offset = 0.08

plt.stem(
    displacement - offset,
    practical_pmf,
    linefmt='C0-',
    markerfmt='C0o',
    basefmt='k-',
    label='Practical PMF'
)

plt.stem(
    displacement + offset,
    theoretical_pmf,
    linefmt='C1-',
    markerfmt='C1s',
    basefmt='k-',
    label='Theoretical PMF'
)

plt.xlabel("Net displacement")
plt.ylabel("Probability")
plt.title("Theoretical and Practical PMF of a Five-Step Random Walk")

plt.xticks(displacement)
plt.legend()
plt.grid(True)

plt.savefig("random_walk_pmf.png", dpi=300, bbox_inches="tight")
plt.close()
