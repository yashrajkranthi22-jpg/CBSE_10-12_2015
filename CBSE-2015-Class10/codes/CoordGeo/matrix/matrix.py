"""A small helper for dot products of coordinate vectors."""

def inner_product(u, v):
    """Multiply matching coordinates and add the products."""
    if len(u) != len(v):
        raise ValueError("vectors must have the same number of coordinates")
    return sum(u_value * v_value for u_value, v_value in zip(u, v))
