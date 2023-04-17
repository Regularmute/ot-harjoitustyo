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

    def get_one_by_character_id(self, character_id):
        target_characters = filter(
            lambda character: character.character_id == character_id, self.characters)

        target_characters_list = list(target_characters)

        if len(target_characters_list) > 0:
            return target_characters_list[0]

        return None

    def create(self, character):
        character.character_id = len(self.characters)
        self.characters.append(character)

        return character

    def update_character_name(self, character_id, new_name):
        target_characters = filter(
            lambda character: character.character_id == character_id, self.characters)

        target_characters_list = list(target_characters)

        if len(target_characters_list) > 0:
            target_characters_list[0].name = new_name

        return

    def update_character_property(self, character_id, statistic, new_value):
        target_characters = filter(
            lambda character: character.character_id == character_id, self.characters)

        target_characters_list = list(target_characters)

        if len(target_characters_list) > 0:
            target_character = target_characters_list[0]
            stat_to_change = getattr(target_character, statistic)
            if isinstance(stat_to_change, int):
                setattr(target_character, statistic, new_value)

        return


class TestCharacterService(unittest.TestCase):
    def setUp(self):
        self.char_bilbo = Character(1, "Bilbo Baggins", 1, 0, 0)
        self.char_naruto = Character(2, "Naruto Uzumaki", 1, 0, 0)
        self.character_service = CharacterService(FakeCharacterRepository())
        self.character_service.create_character(
            self.char_bilbo.creator_id, self.char_bilbo.name)

    def test_create_character_stores_character_correctly(self):
        creator = self.char_naruto.creator_id
        name = self.char_naruto.name

        self.character_service.create_character(creator, name)

        characters = self.character_service.get_characters()

        self.assertEqual(len(characters), 2)
        self.assertEqual(characters[1].creator_id, self.char_naruto.creator_id)
        self.assertEqual(characters[1].name, self.char_naruto.name)
        self.assertEqual(characters[1].level, 1)
        self.assertEqual(characters[1].experience, 0)
        self.assertEqual(characters[1].hit_points, 0)

    def test_get_characters_retrieves_characters_correctly(self):
        characters = self.character_service.get_characters()

        self.assertEqual(len(characters), 1)
        self.assertEqual(characters[0].creator_id, self.char_bilbo.creator_id)
        self.assertEqual(characters[0].name, self.char_bilbo.name)
        self.assertEqual(characters[0].level, self.char_bilbo.level)
        self.assertEqual(characters[0].experience, self.char_bilbo.experience)
        self.assertEqual(characters[0].hit_points, self.char_bilbo.hit_points)

    def test_get_character_by_creator_id_returns_character_correctly(self):
        character = self.character_service.get_character_by_creator_id(1)

        self.assertEqual(character.creator_id, 1)
        self.assertEqual(character.name, self.char_bilbo.name)
        self.assertEqual(character.level, 1)
        self.assertEqual(character.experience, 0)
        self.assertEqual(character.hit_points, 0)

    def test_set_character_name_updates_name_correctly(self):
        id = self.char_bilbo.id
        new_name = "Frodo Baggins"
        self.character_service.set_character_name(id, new_name)

        self.assertEqual(self.char_bilbo.name, "Frodo Baggins")

    def test_set_character_statistic_updates_level_correctly(self):
        id = self.char_bilbo.id
        self.character_service.set_character_statistic(id, "level", 2)

        self.assertEqual(self.char_bilbo.level, 2)
