"""Check the inverse-probability model and integer-count feasibility for C10-Q15."""
from fractions import Fraction
from math import lcm

p_red = Fraction(1, 4)
p_blue = Fraction(1, 3)
orange_count = 10

# The denominator of each prescribed probability constrains the integer total.
required_multiple = lcm(p_red.denominator, p_blue.denominator)
assert required_multiple == 12

# Probability conservation determines the total exactly.
orange_probability = 1 - p_red - p_blue
total = Fraction(orange_count, 1) / orange_probability
assert total.denominator == 1
N = int(total)

red = N * p_red
blue = N * p_blue
orange = orange_count
assert red.denominator == blue.denominator == 1
assert red + blue + orange == N
assert N % required_multiple == 0
assert (red, blue, orange, N) == (6, 8, 10, 24)

print("C10-Q15 integer-feasibility verification: PASS")
print(f"R={red}, B={blue}, O={orange}, N={N}")
