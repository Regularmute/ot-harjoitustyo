import unittest
from repositories.character_repository import character_repository
from entities.character import Character


class TestCharacterRepository(unittest.TestCase):
    def setUp(self):
        character_repository.delete_all()
        self.character_drago = Character(333, "Drago Mastermind", 5, 500, 60)
        self.character_griselda = Character(8241, "Earth Mage Griselda", 7, 200, 58)

    def characters_are_the_same(self, character1, character2):
        return (character1.creator_id == character2.creator_id
                and character1.name == character2.name
                and character1.level == character2.level
                and character1.experience == character2.experience
                and character1.hit_points == character2.hit_points)


    def test_create_stores_character_object_correctly(self):
        character_repository.create(self.character_drago)
        characters = character_repository.get_all()

        self.assertEqual(len(characters), 1)
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )

    def test_get_all_returns_character_objects_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)
        characters = character_repository.get_all()

        self.assertEqual(len(characters), 2)

        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )

        self.assertTrue(
            self.characters_are_the_same(characters[1], self.character_griselda)
        )

    def test_get_one_by_creator_id_gets_correct_character(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        user_id = self.character_drago.creator_id
        fetched_character = character_repository.get_one_by_creator_id(user_id)

        self.assertTrue(
            self.characters_are_the_same(fetched_character, self.character_drago)
        )

    def test_delete_all_empties_table_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_repository.delete_all()
        characters = character_repository.get_all()
        self.assertEqual(len(characters), 0)
