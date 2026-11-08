"""Orthogonal projection/least-squares residual check for C12-Q06."""
import sympy as sp

u = sp.Matrix([2, 3, 4])
w = sp.Matrix([1, 2, 2])
P = sp.simplify(u * (u.T * u)[0]**-1 * u.T)
residual = sp.simplify((sp.eye(3) - P) * w)

assert P == sp.Matrix([[4, 6, 8], [6, 9, 12], [8, 12, 16]]) / 29
assert residual == sp.Matrix([-3, 10, -6]) / 29
assert sp.simplify((u.T * residual)[0]) == 0
distance = sp.sqrt(sp.simplify((residual.T * residual)[0]))
assert distance == sp.sqrt(5) / sp.sqrt(29)

print("C12-Q06 orthogonal-projection verification: PASS")
print("residual =", tuple(residual), "; distance =", distance)
