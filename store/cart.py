"""Cart arithmetic."""
from typing import Dict, List


def cart_total(items: List[Dict]) -> float:
    return round(sum(item["price"] * item["quantity"] for item in items), 2)


def apply_coupon(total: float, percent: float) -> float:
    """Price after a percentage coupon: 10 means 10% off."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(total - percent, 2)
