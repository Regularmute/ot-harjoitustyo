import unittest
from user_service import UserService
from user import User

class FakeUserRepository:
    def __init__(self):
        self.users = []

    def get_all(self):
        return self.users

    def create(self, user):
        self.users.append(user)

        return user

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_steve = User("Steve", "hunter2")
        self.user_service = UserService(FakeUserRepository())

    def test_create_user_stores_username_correctly(self):
        username = self.user_steve.username
        password = self.user_steve.password

        self.user_service.create_user(username, password)

        users = self.user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_steve.username)