import unittest
from repositories.character_repository import character_repository
from entities.character import Character


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        character_repository.delete_all()
        self.character_drago = Character(333, "Drago Mastermind", 5, 500, 60)
        self.character_griselda = Character(8241, "Earth Mage Griselda", 7, 200, 58)

    def test_create_stores_character_object_correctly(self):
        character_repository.create(self.character_drago)
        characters = character_repository.get_all()

        self.assertEqual(len(characters), 1)
        self.assertEqual(characters[0].creator_id, self.character_drago.creator_id)
        self.assertEqual(characters[0].name, self.character_drago.name)
        self.assertEqual(characters[0].level, self.character_drago.level)
        self.assertEqual(characters[0].experience, self.character_drago.experience)
        self.assertEqual(characters[0].hit_points, self.character_drago.hit_points)

    def test_get_all_returns_character_objects_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)
        characters = character_repository.get_all()

        self.assertEqual(len(characters), 2)

        self.assertEqual(characters[0].creator_id, self.character_drago.creator_id)
        self.assertEqual(characters[0].name, self.character_drago.name)
        self.assertEqual(characters[0].level, self.character_drago.level)
        self.assertEqual(characters[0].experience, self.character_drago.experience)
        self.assertEqual(characters[0].hit_points, self.character_drago.hit_points)

        self.assertEqual(characters[1].creator_id, self.character_griselda.creator_id)
        self.assertEqual(characters[1].name, self.character_griselda.name)
        self.assertEqual(characters[1].level, self.character_griselda.level)
        self.assertEqual(characters[1].experience, self.character_griselda.experience)
        self.assertEqual(characters[1].hit_points, self.character_griselda.hit_points)


    def test_get_one_by_creator_id_gets_correct_character(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        user_id = self.character_drago.creator_id
        fetched_character = character_repository.get_one_by_creator_id(user_id)

        self.assertEqual(fetched_character.creator_id, self.character_drago.creator_id)
        self.assertEqual(fetched_character.name, self.character_drago.name)
        self.assertEqual(fetched_character.level, self.character_drago.level)
        self.assertEqual(fetched_character.experience, self.character_drago.experience)
        self.assertEqual(fetched_character.hit_points, self.character_drago.hit_points)

    def test_delete_all_empties_table_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_repository.delete_all()
        characters = character_repository.get_all()
        self.assertEqual(len(characters), 0)
