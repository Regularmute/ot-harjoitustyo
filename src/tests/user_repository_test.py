import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_jaana = User("Jaana", "hashattu2")
        self.user_keijo = User("keijokoo", "hashBROWN1")

    def test_create_stores_user_object_correctly(self):
        user_repository.create(self.user_jaana)
        users = user_repository.get_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_jaana.username)
        self.assertEqual(users[0].password, self.user_jaana.password)