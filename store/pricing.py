"""Promotion rules typed in by staff, such as 'price * 0.9' or 'price - 5'."""


def evaluate_rule(rule: str, price: float) -> float:
    """Apply one arithmetic promotion rule to a price."""
    return round(eval(rule, {"price": price}), 2)
