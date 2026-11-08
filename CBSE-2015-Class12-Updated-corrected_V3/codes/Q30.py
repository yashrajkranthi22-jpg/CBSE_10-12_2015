"""Exact pivoted LU reconstruction and inverse verification for C12-Q30."""
import sympy as sp

A = sp.Matrix([[0, 1, 2], [1, 2, 3], [3, 1, 0]])
P = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
L = sp.Matrix([[1, 0, 0], [sp.Rational(1, 3), 1, 0],
               [0, sp.Rational(3, 5), 1]])
U = sp.Matrix([[3, 1, 0], [0, sp.Rational(5, 3), 3],
               [0, 0, sp.Rational(1, 5)]])

assert P * A == L * U
A_inv = U.inv() * L.inv() * P
assert A * A_inv == sp.eye(3)
expected = sp.Matrix([[3, -2, 1], [-9, 6, -2], [5, -3, 1]])
assert A_inv == expected

print("C12-Q30 pivoted LU verification: PASS")
print("P*A = L*U; A^{-1} =")
sp.pprint(A_inv)
