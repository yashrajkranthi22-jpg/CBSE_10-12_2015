"""Check the binomial-probability relation after deriving p = 1/4."""
from math import comb

p = 1 / 4
q = 1 - p
p_exactly_two = comb(3, 2) * p**2 * q
p_exactly_three = p**3
print("P(X=2):", p_exactly_two)
print("9 * P(X=3):", 9 * p_exactly_three)
