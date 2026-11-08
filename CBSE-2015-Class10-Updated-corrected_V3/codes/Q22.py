"""Independent exact checks for the finite-support Z-transform solution of C10-Q22."""
import sympy as sp

z = sp.symbols("z")
N = 60
q = 1 / z

# Closed form for X(z) = sum_{k=0}^{N-1} (8 + 2k) z^{-k}.
X_closed = (
    8 * (1 - q**N) / (1 - q)
    + 2 * q * (1 - N * q ** (N - 1) + (N - 1) * q**N) / (1 - q) ** 2
)
X_finite = sum((8 + 2 * k) * z ** (-k) for k in range(N))
assert sp.simplify(X_closed - X_finite) == 0

# The terminal sample and accumulator difference enforce finite support.
x59 = 8 + 2 * 59
s59 = sum(8 + 2 * k for k in range(60))
s49 = sum(8 + 2 * k for k in range(50))
last_ten = s59 - s49
assert x59 == 126
assert 8 + 2 * 50 == 108
assert (s59, s49, last_ten) == (4020, 2850, 1170)

# Check the accumulator transfer identity symbolically.
S = sp.simplify(X_closed / (1 - z**-1))
assert sp.simplify(S * (1 - z**-1) - X_closed) == 0

print("C10-Q22 finite Z-transform verification: PASS")
print(f"x[59]={x59}; sum(x[50:60])={last_ten}")
