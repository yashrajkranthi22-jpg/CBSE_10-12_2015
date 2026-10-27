"""Check the Q37 values found by hand using Gaussian elimination."""
# Keep the numerical check tied to the values established in the solution.
import numpy as np

# Gaussian elimination in the written solution gives u = Rs. 300 and
# v = Rs. 1500. Here we only substitute those theoretical values into the system.
coefficients = np.array([[1.0, 1.0], [1.0, 0.0]])
right_hand_side = np.array([1800.0, 300.0])
theoretical_answer = np.array([300.0, 1500.0])
deposit = 15000.0
monthly_rate = 0.10

print("system residual (should be [0, 0]):", coefficients @ theoretical_answer - right_hand_side)
print("interest-rate residual (should be 0):", theoretical_answer[1] - deposit * monthly_rate)
print("reported monthly rate:", monthly_rate * 100, "%")
