"""Verify the forward and backward unilateral-Laplace solutions of C12-Q24."""
import sympy as sp

s, sigma, rho, x = sp.symbols("s sigma rho x", real=True)
u0 = -sp.pi**3 / 27

# Forward coordinate sigma = tau - tau_0: u_sigma + u = 0.
U_forward = u0 / (s + 1)
u_forward = sp.inverse_laplace_transform(U_forward, s, sigma, noconds=True)
assert sp.simplify(u_forward - u0 * sp.exp(-sigma)) == 0

# Backward coordinate rho = tau_0 - tau: u_rho - u = 0.
U_backward = u0 / (s - 1)
u_backward = sp.inverse_laplace_transform(U_backward, s, rho, noconds=True)
assert sp.simplify(u_backward - u0 * sp.exp(rho)) == 0

# Both branches map to the same x-domain expression on cos(x) > 0.
u_x = -2 * sp.pi**3 * sp.cos(x) / 27
y = x**3 + u_x
residual = sp.trigsimp(sp.diff(y, x) + y * sp.tan(x) - (3*x**2 + x**3*sp.tan(x)))
initial_value = sp.simplify(y.subs(x, sp.pi/3))
assert sp.simplify(residual) == 0
assert initial_value == 0

tau = sp.log(1 / sp.cos(x))
sigma_x = tau - sp.log(2)
rho_x = sp.log(2) - tau
assert sp.trigsimp(sp.exp(-sigma_x) - 2*sp.cos(x)) == 0
assert sp.trigsimp(sp.exp(rho_x) - 2*sp.cos(x)) == 0

print("C12-Q24 forward/backward Laplace verification: PASS")
print("Original ODE residual:", residual)
print("Initial condition:", initial_value)
print("Solution: y = x**3 - (2*pi**3/27)*cos(x)")
