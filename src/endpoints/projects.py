# src/squirrelpy/endpoints/projects.py

from typing import Any, Dict
from ..models import Project
from ..exceptions import SquirrelNotFoundError


class ProjectsEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self, project_id: str) -> Project:
        data = self.client.get(f"/projects/{project_id}")

        if not data:
            raise SquirrelNotFoundError(f"Project {project_id} not found.")

        return Project(**data)

    def list(self):
        items = self.client.get("/projects")
        return [Project(**item) for item in items]

    def create(self, name: str, metadata: Dict[str, Any] = None):
        payload = {"name": name, "metadata": metadata}
        data = self.client.post("/projects", json=payload)
        return Project(**data)
