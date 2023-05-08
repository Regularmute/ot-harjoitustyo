"""Hahmo-olioiden sovelluslogiikka.

Kutsuu character_repository.py:tä tietokannan käsittelemistä varten.
"""

from repositories.character_repository import (
    character_repository as default_character_repository
)
from entities.character import Character

class ValueTypeError(Exception):
    """Muuttujan arvo on väärää tyyppiä."""

class NegativeValueError(Exception):
    """Muuttujan täytyy olla positiivinen."""


class CharacterService:
    def __init__(
        self,
        character_repository=default_character_repository
    ):

        self._character_repository = character_repository

    def create_character(self, creator_id, name):
        character = self._character_repository.create(
            Character(creator_id, name, "Human", "Skilled", 1, 0, 1))

        return character

    def get_characters(self):
        """Hakee tietokannasta kaikki hahmot.

        Returns:
            Lista jokaisen tietokannan rivin tiedoista muodostetuista
            hahmoolioista.
        """

        return self._character_repository.get_all()

    def get_character_by_creator_id(self, creator_id):
        """VANHENTUNUT: Hakee tietokannasta tietyn käyttäjän ylimmän hahmon.

        Args:
            creator_id(int): Hahmon luoneen käyttäjän tunnisteluku.

        Returns:
            Käyttäjän luoma hahmo-olio joka on ylimpänä tietokannassa.
        """
        return self._character_repository.get_one_by_creator_id(creator_id)

    def get_all_by_creator_id(self, creator_id):
        """Hakee tietokannasta kaikki tietyn käyttäjän luomat hahmot.

        Args:
            creator_id(int): Hahmojen luoneen käyttäjän tunnisteluku.

        Returns:
            Lista hahmo-olioista jotka parametrin käyttäjä on luonut.
        """

        return self._character_repository.get_all_by_creator_id(creator_id)

    def get_character_by_character_id(self, char_id):
        """Hakee tietokannasta tietyn hahmon tunnisteluvun perusteella.

        Args:
            char_id(int): Haettavan hahmon tunnisteluku.

        Returns:
            Hahmo-olio, jolla on vastaava tunnisteluku.
        """

        return self._character_repository.get_one_by_character_id(char_id)

    def set_character_name(self, character_id, new_name):
        """Muokkaa hahmon nimeä tietokannassa.

        Args:
            character_id(int): Muokattavan hahmon tunnisteluku.
            new_name(str): Uusi nimi joka annetaan hahmolle.
        """
        self._character_repository.update_character_name(
            character_id, new_name)

    def set_character_attribute_float(self, character_id, attribute, new_value):
        """Muokkaa jotakin hahmon numeraalista ominaisuutta tietokannassa.

        Args:
            character_id(int): Muokattavan hahmon tunnisteluku.
            attribute(str): Ominaisuus, jota halutaan muokata.
            new_value(float): Uusi arvo muokattavalle ominaisuudelle.
        """

        try:
            float(new_value)
        except ValueTypeError as exc:
            raise ValueTypeError("New value must be a number") from exc

        if float(new_value) < 0:
            raise NegativeValueError("Value must be positive")

        self._character_repository.update_character_property(
            character_id, attribute, float(new_value))


character_service = CharacterService()
