# src/squirrelpy/endpoints/assets.py

from typing import Any, Dict
from ..models import Asset
from ..exceptions import SquirrelNotFoundError


class AssetsEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self, asset_id: str) -> Asset:
        data = self.client.get(f"/assets/{asset_id}")

        if not data:
            raise SquirrelNotFoundError(f"Asset {asset_id} not found.")

        return Asset(**data)

    def list(self, project_id: str):
        items = self.client.get(f"/projects/{project_id}/assets")
        return [Asset(**item) for item in items]

    def upload(self, project_id: str, filename: str, content: bytes, metadata: Dict[str, Any] = None):
        payload = {
            "filename": filename,
            "content": content.decode("utf-8"),
            "metadata": metadata,
        }

        data = self.client.post(f"/projects/{project_id}/assets", json=payload)
        return Asset(**data)
