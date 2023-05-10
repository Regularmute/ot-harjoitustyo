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

class MissingParamError(Exception):
    """Tarvittava muuttuja puuttuu."""


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

    def set_character_attribute_string(self, character_id, attribute, new_value):
        """Muokkaa jotakin hahmon merkkijono-ominaisuutta tietokannassa.

        Args:
            character_id(int): Muokattavan hahmon tunnisteluku.
            attribute(str): Ominaisuus, jota halutaan muokata.
            new_string(str): Uusi merkkijono muokattavalle ominaisuudelle.
        """

        if not new_value:
            raise MissingParamError("new_value cannot be empty.")

        new_string = str(new_value)
        self._character_repository.update_character_column(
            character_id, attribute, new_string)

    def set_character_attribute_float(self, character_id, attribute, new_value):
        """Muokkaa jotakin hahmon numeraalista ominaisuutta tietokannassa.

        Funktio kokeilee muokata syötetyn arvon merkkijonosta liukuluvuksi.
        Jos merkkijonosta ei voi tehdä liukulukua, syntyvä virhe napataan
        ja käyttöjärjestelmälle ilmoitetaan virhe, jonka se ilmoittaa
        käyttäjälle.

        Args:
            character_id(int): Muokattavan hahmon tunnisteluku.
            attribute(str): Ominaisuus, jota halutaan muokata.
            new_value(float): Uusi arvo muokattavalle ominaisuudelle.
        """

        try:
            float(new_value)
        except ValueError as exc:
            raise ValueTypeError("New value must be a number") from exc

        if float(new_value) < 0:
            raise NegativeValueError("Value must be positive")

        self._character_repository.update_character_column(
            character_id, attribute, float(new_value))

    def delete_character_by_id(self, character_id):
        """Poistaa tiettyä tunnistelukua vastaavan hahmon tietokannasta.

        Args:
            character_id(str): Poistettavan hahmon tunnisteluku.
        """

        self._character_repository.delete_character_by_id(character_id)

    def delete_all_characters(self):
        """Poistaa kaikki hahmot tietokannasta."""

        self._character_repository.delete_all()


character_service = CharacterService()
