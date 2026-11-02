"""Low-stock alerts for the warehouse team."""

ALERT_AT = 5


def needs_restock(units_left: int) -> bool:
    """Alert when 5 or fewer units are left."""
    return units_left <= ALERT_AT
