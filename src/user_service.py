from user_repository import (
    user_repository as default_user_repository
)

class UserService:
    def __init__(
        self,
        user_repository=default_user_repository
    ):

        self._user_repository = user_repository

    def create_user(self, username, password):
        self._user_repository.create(username, password)

user_service = UserService()