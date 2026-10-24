"""Check the arithmetic-progression calculations for Q11."""
# These are the first term and common difference obtained in the solution.
first_term = 2
common_difference = -2

# The nth term is a + (n - 1)d.
term_14 = first_term + 13 * common_difference
term_8 = first_term + 7 * common_difference
term_6 = first_term + 5 * common_difference

# The sum of n terms is n/2 * (2a + (n - 1)d).
sum_20 = 20 / 2 * (2 * first_term + 19 * common_difference)

assert term_14 == 2 * term_8
assert term_6 == -8
assert sum_20 == -340
print(f"Q11: t14={term_14}, t8={term_8}, t6={term_6}, S20={sum_20:.0f}")
