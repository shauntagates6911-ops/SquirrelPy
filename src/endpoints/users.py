# src/squirrelpy/endpoints/users.py

from ..models import User
from ..exceptions import SquirrelNotFoundError


class UsersEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self, user_id: str) -> User:
        data = self.client.get(f"/users/{user_id}")

        if not data:
            raise SquirrelNotFoundError(f"User {user_id} not found.")

        return User(**data)

    def list(self):
        items = self.client.get("/users")
        return [User(**item) for item in items]
