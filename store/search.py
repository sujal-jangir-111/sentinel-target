"""Product search for the shop's search box."""
from typing import Dict, List

PRODUCTS: List[Dict] = [
    {"sku": "SKU-1", "name": "Widget"},
    {"sku": "SKU-2", "name": "Gadget Pro"},
    {"sku": "SKU-3", "name": "Mini Widget"},
]


def search(query: str) -> List[str]:
    """SKUs whose name contains the query. Customers type in any case."""
    return [p["sku"] for p in PRODUCTS if query in p["name"]]
