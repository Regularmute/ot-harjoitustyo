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

    def test_get_all_returns_user_objects_correctly(self):
        user_repository.create(self.user_jaana)
        user_repository.create(self.user_keijo)
        users = user_repository.get_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_jaana.username)
        self.assertEqual(users[0].password, self.user_jaana.password)
        self.assertEqual(users[1].username, self.user_keijo.username)
        self.assertEqual(users[1].password, self.user_keijo.password)

    def test_get_one_by_username_returns_correct_user(self):
        user_repository.create(self.user_jaana)
        user_repository.create(self.user_keijo)
        fetched_user = user_repository.get_one_by_username("keijokoo")

        self.assertEqual(fetched_user.username, self.user_keijo.username)
        self.assertEqual(fetched_user.password, self.user_keijo.password)

    def test_delete_all_empties_table_correctly(self):
        user_repository.create(self.user_jaana)
        user_repository.create(self.user_keijo)

        user_repository.delete_all()
        users = user_repository.get_all()
        self.assertEqual(len(users), 0)
