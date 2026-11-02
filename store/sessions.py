"""Customer sessions kept in a cookie."""
import base64
import pickle
from typing import Dict


def dump_session(data: Dict) -> str:
    return base64.b64encode(pickle.dumps(data)).decode()


def load_session(cookie: str) -> Dict:
    """The session stored in the customer's cookie."""
    return pickle.loads(base64.b64decode(cookie))
