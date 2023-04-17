from repositories.character_repository import (
    character_repository as default_character_repository
)
from entities.character import Character


class CharacterService:
    def __init__(
        self,
        character_repository=default_character_repository
    ):

        self._character_repository = character_repository

    def create_character(self, creator_id, name):
        character = self._character_repository.create(Character(creator_id, name, 1, 0, 0))

        return character

    def get_characters(self):
        return self._character_repository.get_all()

    def get_character_by_creator_id(self, creator_id):
        return self._character_repository.get_one_by_creator_id(creator_id)


character_service = CharacterService()
