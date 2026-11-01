"""Builds the invoice shown after checkout."""
from typing import Dict

from store.tax import calculate_tax


def build_invoice(subtotal: float, region: str = "US") -> Dict[str, float]:
    """Subtotal, tax for the customer's region, and total."""
    tax = calculate_tax(subtotal)
    return {"subtotal": subtotal, "tax": tax, "total": round(subtotal + tax, 2)}
