"""Null-space/rank-nullity verification for C12-Q01."""
import sympy as sp

M = sp.Matrix([[1, -2, -3], [3, -1, -2]])
assert M.rank() == 2
basis = M.nullspace()
assert len(basis) == 1
v = basis[0]
assert M * v == sp.zeros(2, 1)
assert v == sp.Matrix([1, -7, 5])
assert sp.sqrt((v.T * v)[0]) == 5 * sp.sqrt(3)

scale = sp.sqrt(171) / sp.sqrt((v.T * v)[0])
d = sp.simplify(scale * v)
assert sp.simplify(sp.sqrt((d.T * d)[0]) - sp.sqrt(171)) == 0
assert M * d == sp.zeros(2, 1)

print("C12-Q01 null-space verification: PASS")
print("rank(M) =", M.rank(), "; nullity =", 3-M.rank())
print("d =", d.T, "or its negative")
