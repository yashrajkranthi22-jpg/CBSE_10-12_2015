"""Check the two conditional probabilities used in Question 57."""
# Keep the numerical check tied to the values established in the solution.

# First ball red: add two red, leaving 5 red and 5 black.
red_then_two_red = (3/8) * (5/10) * (4/9)
# First ball black: add two black, leaving 3 red and 7 black.
black_then_two_red = (5/8) * (3/10) * (2/9)
answer = red_then_two_red + black_then_two_red
print("red-first contribution:", red_then_two_red)
print("black-first contribution:", black_then_two_red)
print("total probability:", answer, "(theoretical value: 1/8)")
