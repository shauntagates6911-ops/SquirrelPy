# src/squirrelpy/utils.py

from typing import Any, Dict


def snake_to_camel(s: str) -> str:
    """
    Converts snake_case to camelCase.
    Example:
        "project_name" -> "projectName"
    """
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def camel_to_snake(s: str) -> str:
    """
    Converts camelCase to snake_case.
    Example:
        "projectName" -> "project_name"
    """
    snake = ""
    for char in s:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake


def filter_none(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Removes keys with None values from a dictionary.
    Useful for cleaning API payloads.
    """
    return {k: v for k, v in data.items() if v is not None}


def pretty_json(data: Dict[str, Any]) -> str:
    """
    Returns a pretty-printed JSON string.
    Great for debugging API responses.
    """
    import json
    return json.dumps(data, indent=4, sort_keys=True)
