"""HTTP routes for the store features."""
from typing import Dict, List

from fastapi import APIRouter

from store import cart, downloads, inventory, invoice, orders, pricing, reports, shipping, users, wishlist

router = APIRouter(prefix="/api/store")
SAMPLE_ORDERS: List[Dict] = []


@router.get("/reports/average")
async def average() -> Dict[str, float]:
    return {"average": reports.average_order_value(SAMPLE_ORDERS)}


@router.get("/coupon")
async def coupon(total: float, percent: float) -> Dict[str, float]:
    return {"total": cart.apply_coupon(total, percent)}


@router.get("/orders")
async def order_page(page: int = 1) -> List[Dict]:
    return orders.paginate(SAMPLE_ORDERS, page)


@router.get("/invoice/{name}")
async def invoice_file(name: str) -> Dict[str, str]:
    return {"content": downloads.read_invoice(name)}


@router.get("/invoice-preview")
async def invoice_preview(subtotal: float, region: str = "US") -> Dict[str, float]:
    return invoice.build_invoice(subtotal, region)


@router.get("/reserve")
async def reserve(sku: str, quantity: int = 1) -> Dict[str, bool]:
    return {"reserved": inventory.reserve(sku, quantity)}


@router.get("/shipping")
async def shipping_price(subtotal: float) -> Dict[str, float]:
    return {"shipping": shipping.shipping_cost(subtotal)}


@router.get("/promo")
async def promo(rule: str, price: float) -> Dict[str, float]:
    return {"price": pricing.evaluate_rule(rule, price)}


@router.post("/wishlist")
async def wishlist_add(item: str) -> List[str]:
    return wishlist.add_item(item)
