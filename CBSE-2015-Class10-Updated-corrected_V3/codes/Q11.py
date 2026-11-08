"""Verify C10-Q11 by the unilateral Z-transform and accumulator."""
import sympy as sp

q = sp.symbols("q")  # q = z^{-1}
a, d = sp.Integer(2), sp.Integer(-2)

# Unilateral transform X(q) = a*q/(1-q) + d*q^2/(1-q)^2.
X = a * q / (1 - q) + d * q**2 / (1 - q) ** 2
series = sp.series(X, q, 0, 21).removeO()
coeff = lambda n: sp.expand(series).coeff(q, n)

assert coeff(6) == -8
assert coeff(14) == 2 * coeff(8)

# The accumulator transfer 1/(1-q) turns the sequence into its partial sums.
S = sp.series(X / (1 - q), q, 0, 21).removeO()
sum_20 = sp.expand(S).coeff(q, 20)
assert sum_20 == -340

print("C10-Q11 unilateral Z-transform verification: PASS")
print("x[6] =", coeff(6), "; x[14] =", coeff(14), "; 2*x[8] =", 2*coeff(8))
print("Accumulator coefficient s[20] =", sum_20)
