"""Use NumPy to check the theoretically derived values for Q8."""
import numpy as np

# The written elimination gives a = 1 and d = 5.
theoretical_values = np.array([1, 5], dtype=float)

# The two conditions S5 + S7 = 167 and S10 = 235 reduce to this system:
# 12a + 31d = 167 and 10a + 45d = 235.
coefficients = np.array([[12, 31],
                         [10, 45]], dtype=float)
right_hand_side = np.array([167, 235], dtype=float)

# NumPy's built-in linear solver independently solves for [a, d].
solved_values = np.linalg.solve(coefficients, right_hand_side)

# Compare the numerical solution with the values already found theoretically.
if np.allclose(solved_values, theoretical_values):
    print("Q8: NumPy confirms the theoretical values a=1 and d=5.")
    print("The arithmetic progression is 1, 6, 11, 16, ...")
else:
    raise ValueError(
        f"Theoretical values do not match the NumPy solution: {solved_values}"
    )
