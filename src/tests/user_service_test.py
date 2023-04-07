import unittest
import bcrypt
from user_service import UserService
from user import User


class FakeUserRepository:
    def __init__(self):
        self.users = []

    def get_all(self):
        return self.users

    def get_one_by_username(self, username):
        target_users = filter(lambda user: user.username == username, self.users)

        target_users_list = list(target_users)

        if len(target_users_list) > 0:
            return target_users_list[0]

        return None

    def create(self, user):
        self.users.append(user)

        return user


class TestUserService(unittest.TestCase):
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

    def test_create_user_does_not_store_password_in_plain_text(self):
        username = self.user_steve.username
        password = self.user_steve.password

        self.user_service.create_user(username, password)

        users = self.user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertNotEqual(users[0].password, self.user_steve.password)

    def test_create_user_stores_hashed_password_correctly(self):
        username = self.user_steve.username
        password = self.user_steve.password

        self.user_service.create_user(username, password)

        byte_password = password.encode('utf-8')
        users = self.user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertTrue(bcrypt.checkpw(byte_password, users[0].password))
