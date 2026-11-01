"""Shipping charges."""

FREE_SHIPPING_FROM = 50.0
FLAT_RATE = 4.99


def shipping_cost(subtotal: float) -> float:
    """Orders of $50 or more ship free; everything else pays the flat rate."""
    return 0.0 if subtotal >= FREE_SHIPPING_FROM else FLAT_RATE
