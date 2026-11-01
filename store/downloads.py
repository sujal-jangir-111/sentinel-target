"""Invoice downloads."""
import os

INVOICE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "invoices")


def read_invoice(name: str) -> str:
    """Contents of one file from INVOICE_DIR."""
    path = os.path.join(INVOICE_DIR, name)
    with open(path, encoding="utf-8") as handle:
        return handle.read()
