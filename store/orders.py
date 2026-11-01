"""Order listing for the customer's order history page."""
from typing import Dict, List


def paginate(orders: List[Dict], page: int, size: int = 20) -> List[Dict]:
    """One page of orders. Pages are numbered from 1."""
    if page < 1:
        raise ValueError("page starts at 1")
    start = page * size
    return orders[start:start + size]
