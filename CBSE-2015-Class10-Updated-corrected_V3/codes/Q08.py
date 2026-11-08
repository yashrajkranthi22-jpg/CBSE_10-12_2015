"""Verify the Jacobi iteration and spectral-radius convergence for C10-Q08."""
import numpy as np

A = np.array([[12.0, 31.0], [10.0, 45.0]])
b = np.array([167.0, 235.0])
D = np.diag(np.diag(A))
R = A - D
T = -np.linalg.inv(D) @ R
c = np.linalg.solve(D, b)

eigenvalues = np.linalg.eigvals(T)
spectral_radius = max(abs(eigenvalues))
assert np.isclose(spectral_radius, np.sqrt(31 / 54))
assert spectral_radius < 1.0

x = np.zeros(2)
history = []
for k in range(1, 501):
    x_next = T @ x + c
    increment = np.linalg.norm(x_next - x, ord=np.inf)
    residual = np.linalg.norm(b - A @ x_next, ord=np.inf)
    if k in (1, 2, 10, 20, 40, 60):
        history.append((k, x_next.copy(), residual))
    x = x_next
    if increment < 1e-8:
        history.append((k, x.copy(), residual))
        break
else:
    raise RuntimeError("Jacobi iteration did not meet the stopping criterion")

assert k == 77
assert np.allclose(x, [1.0, 5.0], atol=2e-8)
assert np.linalg.norm(b - A @ x, ord=np.inf) < 2e-7

for iteration, values, residual in history:
    print(f"k={iteration:3d}: a={values[0]:.8f}, d={values[1]:.8f}, "
          f"||b-Ax||_inf={residual:.3e}")
print(f"rho(T_J)={spectral_radius:.9f}; stopping iteration={k}")
print("C10-Q08 Jacobi verification: PASS; AP = 1, 6, 11, 16, ...")
