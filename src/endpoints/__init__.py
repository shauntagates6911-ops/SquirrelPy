# src/squirrelpy/endpoints/__init__.py

from .projects import ProjectsEndpoint
from .users import UsersEndpoint
from .assets import AssetsEndpoint

__all__ = [
    "ProjectsEndpoint",
    "UsersEndpoint",
    "AssetsEndpoint",
]
