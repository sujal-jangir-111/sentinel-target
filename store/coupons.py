"""Coupon validity."""
from datetime import date


def is_valid(expires_on: date, today: date) -> bool:
    """A coupon can be used up to and including its expiry date."""
    return today < expires_on
