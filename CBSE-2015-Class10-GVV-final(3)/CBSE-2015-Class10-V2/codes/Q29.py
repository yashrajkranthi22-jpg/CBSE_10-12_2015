"""Plot triangles using the two k values found theoretically in Q29."""
import matplotlib.pyplot as plt
import numpy as np

from CoordGeo.line.funcs import line_gen

# Enter the coefficients from the equations derived above.
A = np.array([1.0, -1.0])
valid_k_values = [3.0, -4.5]  # Values obtained from the area equation in the written solution.


def display_number(value):
    """Show whole-number coordinates as 3 rather than 3.0."""
    return int(value) if value.is_integer() else value


fig, axes = plt.subplots(1, 2, figsize=(7.25, 3.65))
for ax, k in zip(axes, valid_k_values):
    # Substitute each theoretically derived k into the coordinates from the question.
    B = np.array([-4.0, 2.0 * k])
    C = np.array([-k, -5.0])

    # The actual CoordGeo library generates each side from its endpoint coordinates.
    for start, end in ((A, B), (B, C), (C, A)):
        side = line_gen(start, end)
        ax.plot(side[0], side[1])
    ax.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], alpha=0.12)
    ax.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], s=22, zorder=3)

    # CoordGeo has no triangle-area function in this upstream version, so use the coordinate formula.
    triangle_area = abs((B[0] - A[0]) * (C[1] - A[1])
                        - (B[1] - A[1]) * (C[0] - A[0])) / 2

    # Small offsets keep the labels separate from the plotted points.
    point_labels = [
        ("A", A, 0.15, 0.18),
        ("B", B, -0.7 if B[1] < 0 else -0.55,
         -0.55 if B[1] < 0 else 0.3),
        ("C", C, 0.13, -0.35 if C[1] < -2 else 0.15),
    ]
    for name, point, dx, dy in point_labels:
        shown_point = tuple(display_number(float(value)) for value in point)
        ax.text(point[0] + dx, point[1] + dy,
                f"{name}{shown_point}", fontsize=7.2)

    k_label = r"3" if k == 3 else r"-\frac{9}{2}"
    ax.set_title(rf"$k={k_label}$; area $={triangle_area:g}$", fontsize=9)
    ax.axhline(0)
    ax.axvline(0)
    ax.grid(True, alpha=0.2)
# These values come from the cases counted in the written solution.
    x_values = [A[0], B[0], C[0]]
    y_values = [A[1], B[1], C[1]]
    ax.set_xlim(min(x_values) - 1.3, max(x_values) + 1.45)
    ax.set_ylim(min(y_values) - 1.45, max(y_values) + 1.45)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x", fontsize=8)
    ax.set_ylabel("y", fontsize=8)
    ax.tick_params(labelsize=7)

fig.suptitle("Q29: Triangles for both valid values of k", fontsize=10)
fig.tight_layout()
fig.savefig("figs/Q29_Triangles.png", dpi=220, bbox_inches="tight")
plt.close(fig)
print("Q29: plotted the triangles for the theoretically derived values k=3 and k=-9/2.")
