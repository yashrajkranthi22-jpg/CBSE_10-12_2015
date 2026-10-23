"""Check the 60th term and sum of the last ten terms in Q22."""
first_term = 8
common_difference = 2
last_term_number = 60

# Use a + (n - 1)d to find the required terms in the progression.
term_60 = first_term + (last_term_number - 1) * common_difference
term_51 = first_term + (51 - 1) * common_difference

# Terms 51 through 60 form an AP of 10 terms; sum = n(first + last)/2.
last_ten_sum = 10 * (term_51 + term_60) / 2
assert term_60 == 126
assert term_51 == 108
assert last_ten_sum == 1170
print(f"Q22: t60={term_60}, t51={term_51}, sum of last 10 terms={last_ten_sum:.0f}")
