"""Verify the inverse matrix obtained by row-reducing Question 30."""
import numpy as np

A = np.array([[0, 1, 2], [1, 2, 3], [3, 1, 0]], dtype=int)
A_inverse = np.array([[3, -2, 1], [-9, 6, -2], [5, -3, 1]], dtype=int)
print("A times A_inverse:")
print(A @ A_inverse)
