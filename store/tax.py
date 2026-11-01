"""Sales tax by region."""

RATES = {"US": 0.08, "DE": 0.19, "IN": 0.18}


def calculate_tax(amount: float, region: str) -> float:
    return round(amount * RATES[region], 2)
