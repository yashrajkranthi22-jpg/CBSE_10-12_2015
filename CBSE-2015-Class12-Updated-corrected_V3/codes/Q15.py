"""Affine-system/rank-consistency verification for C12-Q15."""
import sympy as sp

A = sp.Matrix([
    [1, 0, 0, -2],
    [0, 1, 0, 3],
    [0, 0, 1, -5],
    [2, 1, 1, 0],
])
b = sp.Matrix([3, 4, 1, 7])
assert A.rank() == A.row_join(b).rank() == 4
sol = A.LUsolve(b)
assert sol == sp.Matrix([sp.Rational(5, 3), 6, sp.Rational(-7, 3), sp.Rational(-2, 3)])

print("C12-Q15 affine intersection verification: PASS")
print("x,y,z,t =", tuple(sol))
