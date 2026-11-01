"""Sales tax."""


def calculate_tax(amount: float) -> float:
    return round(amount * 0.08, 2)
