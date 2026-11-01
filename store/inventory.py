"""Stock reservations."""
from typing import Dict

STOCK: Dict[str, int] = {"SKU-1": 5, "SKU-2": 2}


def reserve(sku: str, quantity: int) -> bool:
    """Reserve stock. True when reserved, False when there isn't enough or the SKU is unknown."""
    if STOCK[sku] > quantity:
        STOCK[sku] -= quantity
        return True
    return False
