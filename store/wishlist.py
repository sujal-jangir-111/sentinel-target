"""Customer wishlists."""
from typing import List


def add_item(item: str, items: List[str] = []) -> List[str]:
    """Add an item to a wishlist, starting a new wishlist when none is given."""
    items.append(item)
    return items
