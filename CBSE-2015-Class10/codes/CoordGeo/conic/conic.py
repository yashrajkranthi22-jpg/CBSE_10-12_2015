"""A small helper for checking a point's position relative to a circle."""

def circle_power(point, centre, radius):
    """Return distance(point, centre)^2 - radius^2.

    A positive result is outside the circle, zero is on it, and a negative
    result is inside it.
    """
    if len(point) != 2 or len(centre) != 2:
        raise ValueError("point and centre must be 2D coordinates")

    squared_distance = sum((x - y) ** 2 for x, y in zip(point, centre))
    return squared_distance - radius ** 2
