import bcrypt
from user_repository import (
    user_repository as default_user_repository
)
from user import User

class InvalidCredentialsError:
    pass

class UsernameExistsError:
    pass

class UserService:
    def __init__(
        self,
        user_repository=default_user_repository
    ):

        self._user_repository = user_repository
        self._user = None

    def create_user(self, username, password):
        self._user_repository.create(User(username, password))

    def get_users(self):
        return self._user_repository.get_all()

    def login(self, username, password):
        byte_password = password.encode('utf-8')
        user = self._user_repository.get_one_by_username(username)

        if not user or not bcrypt.checkpw(byte_password, user.password):
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user


user_service = UserService()
