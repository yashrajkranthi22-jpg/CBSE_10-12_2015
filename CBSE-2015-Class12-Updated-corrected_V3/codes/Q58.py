"""Check the theoretically derived Bayes result for Question 58."""
# Keep the numerical check tied to the values established in the solution.
from fractions import Fraction

p_actual_four = Fraction(1, 6)
p_reports_four_if_four = Fraction(3, 5)
# If he lies, assume each of the other five face values is equally likely.
p_reports_four_if_not_four = Fraction(2, 5) * Fraction(1, 5)

# The written solution gives posterior probability 3/5; verify Bayes' identity.
theoretical_posterior = Fraction(3, 5)
numerator = p_actual_four * p_reports_four_if_four
denominator = numerator + Fraction(5, 6) * p_reports_four_if_not_four
print("posterior identity residual:", theoretical_posterior*denominator - numerator)
print("theoretical posterior:", theoretical_posterior, "(required: 3/5)")
