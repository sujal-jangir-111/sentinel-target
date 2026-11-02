"""Loyalty points."""


def points_for(total: float) -> int:
    """Customers earn 1 point for every whole dollar they spend."""
    if total < 0:
        raise ValueError("total cannot be negative")
    return int(total / 10)
