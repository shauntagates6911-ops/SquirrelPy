# src/squirrelpy/auth.py

from typing import Optional
from .exceptions import SquirrelAuthError


class SquirrelAuth:
    """
    SquirrelAuth — Handles API key validation and token formatting.

    Usage:
        auth = SquirrelAuth("MY_API_KEY")
        header = auth.get_auth_header()
    """

    def __init__(self, api_key: Optional[str]):
        if not api_key or not isinstance(api_key, str):
            raise SquirrelAuthError("A valid API key must be provided.")

        self.api_key = api_key.strip()

    def get_auth_header(self) -> dict:
        """
        Returns the Authorization header used by SquirrelPy.
        """
        return {"Authorization": f"Bearer {self.api_key}"}

    def is_valid(self) -> bool:
        """
        Basic validation check for API key format.
        """
        return len(self.api_key) > 10  # simple sanity check
