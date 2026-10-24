"""Verify the particular solution of Question 24 by substitution."""
import sympy as sp

x = sp.symbols("x", real=True)
C = -2 * sp.pi**3 / 27
y = x**3 + C * sp.cos(x)  # Constant fixed by y(pi/3) = 0.
residual = sp.diff(y, x) + y * sp.tan(x) - (3 * x**2 + x**3 * sp.tan(x))
print("ODE residual simplifies to:", sp.trigsimp(residual))
print("initial value:", sp.simplify(y.subs(x, sp.pi / 3)))
