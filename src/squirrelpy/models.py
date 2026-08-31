# src/squirrelpy/models.py

from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class Project:
    """
    Represents a Squirrel API Project.
    """
    id: str
    name: str
    owner_id: str
    created_at: str
    updated_at: str
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class User:
    """
    Represents a Squirrel API User.
    """
    id: str
    username: str
    avatar_url: Optional[str]
    created_at: str
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class Asset:
    """
    Represents an Asset stored in the Squirrel API.
    """
    id: str
    project_id: str
    filename: str
    size: int
    content_type: str
    created_at: str
    metadata: Optional[Dict[str, Any]] = None
