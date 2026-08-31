# src/squirrelpy/client.py

import httpx
from typing import Optional, Any, Dict

from .exceptions import (
    SquirrelAPIError,
    SquirrelAuthError,
    SquirrelRateLimitError,
)


class SquirrelClient:
    """
    SquirrelClient — Main HTTP client for interacting with the Squirrel API.

    Usage:
        client = SquirrelClient(api_key="YOUR_KEY")
        project = client.get("/projects/123")
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.squirrel.dev/v1",
        timeout: int = 10,
    ):
        if not api_key:
            raise SquirrelAuthError("API key is required.")

        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout

        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )

    # -----------------------------
    # Internal request handler
    # -----------------------------
    def _request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ):
        response = self._client.request(
            method=method,
            url=endpoint,
            params=params,
            data=data,
            json=json,
        )

        # Rate limit
        if response.status_code == 429:
            raise SquirrelRateLimitError("Rate limit exceeded.")

        # Auth error
        if response.status_code == 401:
            raise SquirrelAuthError("Invalid API key.")

        # General API error
        if response.status_code >= 400:
            raise SquirrelAPIError(
                f"API Error {response.status_code}: {response.text}"
            )

        return response.json()

    # -----------------------------
    # Public request helpers
    # -----------------------------
    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
