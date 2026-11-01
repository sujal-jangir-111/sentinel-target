"""Order notifications sent to the fulfilment webhook."""
import requests


def post_order(url: str, order_id: str) -> int:
    return requests.post(url, json={"order": order_id}, timeout=5).status_code
