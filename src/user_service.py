from user_repository import (
    user_repository as default_user_repository
)
from user import User

class UserService:
    def __init__(
        self,
        user_repository=default_user_repository
    ):

        self._user_repository = user_repository

    def create_user(self, username, password):
        self._user_repository.create(User(username, password))

    def get_users(self):
        return self._user_repository.get_all()

user_service = UserService()