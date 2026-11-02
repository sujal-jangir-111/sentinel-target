"""Refunds for cancelled orders."""
from typing import Dict


def refund_total(order: Dict) -> float:
    """Money back for a cancelled order: the items plus any shipping paid. Orders collected in store paid no shipping."""
    items = sum(item["price"] * item["quantity"] for item in order["items"])
    return round(items + order["shipping"], 2)
