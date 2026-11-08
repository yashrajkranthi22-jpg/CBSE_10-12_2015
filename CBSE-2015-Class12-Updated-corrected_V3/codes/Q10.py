"""Affine plane-pencil/normal-vector verification for C12-Q10."""
import sympy as sp

lam = sp.symbols("lam")
direction = sp.Matrix([2, -4, 5])
normal = sp.Matrix([2 + 5*lam, 1 - 3*lam, -1 + 4*lam])
solution = sp.solve(sp.Eq((direction.T * normal)[0], 0), lam)
assert solution == [sp.Rational(5, 42)]

l = solution[0]
coeffs = [sp.simplify(v * 42) for v in normal.subs(l)]
constant = sp.Rational(-3, 1) + l * 9
plane = [*coeffs, sp.simplify(constant * 42)]
assert plane == [109, 27, -22, -81]

print("C12-Q10 affine plane-pencil verification: PASS")
print("42 * plane coefficients =", plane)
