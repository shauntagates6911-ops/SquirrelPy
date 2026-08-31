# src/squirrelpy/exceptions.py

class SquirrelError(Exception):
    """
    Base exception for all SquirrelPy errors.
    """
    pass


class SquirrelAPIError(SquirrelError):
    """
    Raised when the Squirrel API returns an error response (4xx or 5xx).
    """
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code


class SquirrelAuthError(SquirrelError):
    """
    Raised when authentication fails (missing or invalid API key).
    """
    pass


class SquirrelRateLimitError(SquirrelError):
    """
    Raised when the API rate limit is exceeded (HTTP 429).
    """
    pass


class SquirrelNotFoundError(SquirrelAPIError):
    """
    Raised when a requested resource does not exist (HTTP 404).
    """
    pass


class SquirrelValidationError(SquirrelAPIError):
    """
    Raised when the API rejects input due to validation errors (HTTP 400).
    """
    pass
