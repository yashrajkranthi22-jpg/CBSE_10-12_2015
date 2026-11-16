import numpy as np

# Coefficients of the equations:
# 12a + 31d = 167
# 10a + 45d = 235

A = np.array([
    [12, 31],
    [10, 45]
], dtype=float)

B = np.array([167, 235], dtype=float)

# Solve the system using NumPy
a, d = np.linalg.solve(A, B)

print("First term (a):", a)
print("Common difference (d):", d)

# Generate the first 10 terms of the AP
n = np.arange(1, 11)
terms = a + (n - 1) * d

print("\nFirst 10 terms of the AP:")
print(terms)

# Calculate the required sums
S5 = np.sum(terms[:5])
S7 = np.sum(terms[:7])
S10 = np.sum(terms[:10])

print("\nVerification:")
print("S5 =", S5)
print("S7 =", S7)
print("S5 + S7 =", S5 + S7)
print("S10 =", S10)

# Verify the given conditions
assert np.isclose(S5 + S7, 167)
assert np.isclose(S10, 235)

print("\nBoth conditions are verified successfully!")
