"""Antisymmetric determinant/cross-product check for C12-Q05."""
import sympy as sp

a = sp.Matrix([1, 4, 2])
b = sp.Matrix([3, -2, 7])
c = sp.Matrix([2, -1, 4])

cross = a.cross(b)
assert cross == sp.Matrix([32, -1, -14])
assert cross.dot(a) == 0 and cross.dot(b) == 0
t = sp.Rational(27, 1) / c.dot(cross)
d = sp.simplify(t * cross)
assert t == 3
assert d == sp.Matrix([96, -3, -42])
assert c.dot(d) == 27

print("C12-Q05 determinant/cross-product verification: PASS")
print("a x b =", tuple(cross), "; d =", tuple(d))
