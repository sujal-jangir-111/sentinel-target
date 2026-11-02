"""Price conversion for international customers."""


def convert(amount: float, rate: float) -> float:
    """Price in another currency, to the nearest cent."""
    return int(amount * rate * 100) / 100
