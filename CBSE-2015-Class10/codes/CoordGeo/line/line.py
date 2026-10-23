"""Small helper functions for coordinate geometry."""

def displacement(p, q):
    """Return the coordinate changes needed to move from p to q."""
    if len(p) != len(q):
        raise ValueError("points must have the same number of coordinates")
    return tuple(q_value - p_value for p_value, q_value in zip(p, q))
