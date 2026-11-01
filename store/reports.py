"""Sales reports for the admin dashboard."""
from collections import defaultdict
from typing import Dict, List


def average_order_value(orders: List[Dict]) -> float:
    """Average order total. A shop with no orders yet reports 0.0."""
    total = sum(order["total"] for order in orders)
    return round(total / len(orders), 2)


def revenue_by_day(orders: List[Dict]) -> Dict[str, float]:
    days: Dict[str, float] = defaultdict(float)
    for order in orders:
        days[order["date"]] += order["total"]
    return dict(days)
