import unittest
import bcrypt
from services.user_service import (
    UserService, InvalidCredentialsError, UsernameExistsError)
from entities.user import User

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_steve = User("Steve", "hunter2")
        self.user_kyle = User("Kyle", "password1")
        self.user_service = UserService()
        self.user_service.delete_all()
        self.user_service.create_user(
            self.user_kyle.username, self.user_kyle.password, False)

    def test_create_user_stores_username_correctly(self):
        username = self.user_steve.username
        password = self.user_steve.password

        self.user_service.create_user(username, password)

        users = self.user_service.get_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[1].username, self.user_steve.username)

    def test_create_user_does_not_store_password_in_plain_text(self):
        username = self.user_steve.username
        password = self.user_steve.password

        self.user_service.create_user(username, password)

        users = self.user_service.get_users()

        self.assertEqual(len(users), 2)
        self.assertNotEqual(users[1].password, self.user_steve.password)

    def test_create_user_stores_hashed_password_correctly(self):
        username = self.user_steve.username
        password = self.user_steve.password

        self.user_service.create_user(username, password)

        byte_password = password.encode('utf-8')
        users = self.user_service.get_users()

        self.assertEqual(len(users), 2)
        self.assertTrue(bcrypt.checkpw(byte_password, users[1].password))

    def test_user_property_is_None_when_not_logged_in(self):
        self.assertIsNone(self.user_service._user)

    def test_valid_login_updates_current_user_property_correctly(self):
        user = self.user_service.login(
            self.user_kyle.username, self.user_kyle.password)

        self.assertEqual(self.user_service._user, user)

    def test_get_current_user_returns_None_when_not_logged_in(self):
        self.assertIsNone(self.user_service.get_current_user())

    def test_get_current_user_returns_logged_user(self):
        self.user_service.login(
            self.user_kyle.username, self.user_kyle.password)

        self.assertEqual(
            self.user_service._user, self.user_service.get_current_user())

    def test_logout_sets_current_user_property_to_None(self):
        # Log in to check that the user property is set before logging out
        user = self.user_service.login(
            self.user_kyle.username, self.user_kyle.password)
        self.assertEqual(self.user_service._user, user)

        # Log out to make sure that the user property is cleared correctly
        self.user_service.logout()
        self.assertIsNone(self.user_service._user)

    def test_create_user_updates_current_user_property_correctly(self):
        user = self.user_service.create_user(
            self.user_steve.username, self.user_steve.password)

        self.assertEqual(self.user_service._user, user)

    def test_create_user_throws_error_with_existing_username(self):
        self.assertRaises(
            UsernameExistsError,
            lambda: self.user_service.create_user("Kyle", "gamer123")
        )

    def test_login_throws_error_with_invalid_credentials(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.user_service.login(
                self.user_steve.username, self.user_steve.password)
        )
