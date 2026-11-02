"""Email bodies built from templates."""
from jinja2 import Template

RECEIPT = Template("Thanks {{ name }}! Your order {{ order }} is confirmed.")


def receipt(name: str, order: str) -> str:
    return RECEIPT.render(name=name, order=order)
