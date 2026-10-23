"""Triangle area helpers for points in the coordinate plane."""

def signed_double_area(a, b, c):
    """Return twice the signed area; its sign depends on point order."""
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))

def area(a, b, c):
    """Return the usual non-negative area of triangle ABC."""
    return abs(signed_double_area(a, b, c)) / 2
