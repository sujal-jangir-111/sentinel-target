"""Customer lookup."""
import sqlite3
from typing import Optional, Tuple


def create_schema(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")


def find_by_email(conn: sqlite3.Connection, email: str) -> Optional[Tuple]:
    query = f"SELECT id, name, email FROM users WHERE email = '{email}'"
    return conn.execute(query).fetchone()
