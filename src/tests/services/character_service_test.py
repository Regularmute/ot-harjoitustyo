import unittest
from services.character_service import CharacterService
from entities.character import Character


class FakeCharacterRepository:
    def __init__(self):
        self.characters = []

    def get_all(self):
        return self.characters

    def get_one_by_creator_id(self, creator_id):
        target_characters = filter(
            lambda character: character.creator_id == creator_id, self.characters)

        target_characters_list = list(target_characters)

        if len(target_characters_list) > 0:
            return target_characters_list[0]

        return None

    def create(self, character):
        self.characters.append(character)

        return character


class TestCharacterService(unittest.TestCase):
    def setUp(self):
        self.char_bilbo = Character("Bob", "Bilbo Baggins", 1, 0, 0)
        self.char_naruto = Character("sanna2", "Naruto Uzumaki", 1, 0, 0)
        self.character_service = CharacterService(FakeCharacterRepository())
        self.character_service.create_character(
            self.char_bilbo.player, self.char_bilbo.name)

    def test_create_character_stores_character_correctly(self):
        player = self.char_naruto.player
        name = self.char_naruto.name

        self.character_service.create_character(player, name)

        characters = self.character_service.get_characters()

        self.assertEqual(len(characters), 2)
        self.assertEqual(characters[1].player, self.char_naruto.player)
        self.assertEqual(characters[1].name, self.char_naruto.name)
        self.assertEqual(characters[1].level, 1)
        self.assertEqual(characters[1].experience, 0)
        self.assertEqual(characters[1].hit_points, 0)
