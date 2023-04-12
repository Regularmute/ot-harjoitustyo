from character_repository import (
    character_repository as default_character_repository
)
from character import Character


class CharacterService:
    def __init__(
        self,
        character_repository=default_character_repository
    ):

        self._character_repository = character_repository

    def create_character(self, name):
        character = self._character_repository.create(Character(name, 1, 0, 0, 0))

        return character

    def get_characters(self):
        return self._character_repository.get_all()

    def get_character_by_name(self, name):
        return self._character_repository.get_one_by_name(name)


character_service = CharacterService()
