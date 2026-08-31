# src/squirrelpy/__init__.py
"""
SquirrelPy — Official Python SDK for the Squirrel API.

This package provides:
- A typed API client
- Authentication helpers
- Endpoint wrappers
- Data models
- Custom exceptions

Import the main client with:
    from squirrelpy import SquirrelClient
"""

from .client import SquirrelClient
from .exceptions import (
    SquirrelAPIError,
    SquirrelAuthError,
    SquirrelRateLimitError,
)
from .models import (
    Project,
    User,
    Asset,
)

__all__ = [
    "SquirrelClient",
    "SquirrelAPIError",
    "SquirrelAuthError",
    "SquirrelRateLimitError",
    "Project",
    "User",
    "Asset",
]

__version__ = "0.1.0"
