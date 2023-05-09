"""Tietokannan hahmotaulukon käsittelylogiikka."""

from database_connection import get_database_connection
from entities.character import Character

def _get_character_by_row(row):
    return Character(
            row["creator_id"],
            row["name"],
            row["ancestry"],
            row["heritage"],
            row["level"],
            row["experience"],
            row["hit_points"],
            row["character_id"]
        ) if row else None

class CharacterRepository:
    def __init__(self, connection):
        """Alustaa logiikan ja yhdistää sen parametrin tietokantaan.

        Attributes:
            _connection = yhteys käsiteltävään SQLite-tietokantaan.
        """
        self._connection = connection

    def get_all(self):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka palauttaa
        listan kaikista hahmoista.

        Returns:
            Lista hahmo-olioista, jotka on luotu suorittamalla
                _get_character_by_row jokaiseen kyselyn palauttamaan riviin.
        """

        cursor = self._connection.cursor()

        cursor.execute("""SELECT character_id, creator_id, name, ancestry,
                heritage, level, experience, hit_points FROM characters;""")
        rows = cursor.fetchall()

        return list(map(_get_character_by_row, rows))

    def get_one_by_name(self, name):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka palauttaa
            hahmon, jolla on tietty nimi.

        Args:
            name (str): Haetun hahmon nimi.

        Returns:
            Hahmo-olio, joka on luotu suorittamalla _get_character_by_row
            kyselyn palauttamaan riviin.
        """
        cursor = self._connection.cursor()

        sql = "SELECT name FROM characters WHERE name = :name"
        cursor.execute(sql, {"name": name})
        row = cursor.fetchone()

        return _get_character_by_row(row)

    def get_one_by_creator_id(self, creator_id):
        """VANHENTUNUT: Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka
            palauttaa hahmon, joka on tietyn käyttäjän luoma. Vanhentunut
            kysely, sillä yhdellä käyttäjällä voi nykyään olla usea hahmo.

        Args:
            creator_id (int): Haetun käyttäjän tunnisteluku.

        Returns:
            Hahmo-olio, joka on luotu suorittamalla _get_character_by_row
            kyselyn palauttamaan riviin.
        """
        cursor = self._connection.cursor()

        sql = """SELECT character_id, creator_id, name, ancestry, heritage,
                level, experience, hit_points FROM characters
                WHERE creator_id=:creator_id"""

        cursor.execute(sql, {"creator_id": creator_id})
        row = cursor.fetchone()

        return _get_character_by_row(row)

    def get_all_by_creator_id(self, creator_id):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka palauttaa
            kaikki tietyn käyttäjän luomat hahmot.

        Args:
            creator_id (int): Haetun käyttäjän tunnisteluku.

        Returns:
            Lista hahmo-olioista, joka on luotu suorittamalla
            _get_character_by_row jokaiseen kyselyn palauttamaan riviin.
        """
        cursor = self._connection.cursor()

        sql = """SELECT character_id, creator_id, name, ancestry, heritage,
                level, experience, hit_points FROM characters
                WHERE creator_id=:creator_id"""

        cursor.execute(sql, {"creator_id": creator_id})
        rows = cursor.fetchall()

        return list(map(_get_character_by_row, rows))

    def get_one_by_character_id(self, character_id):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka palauttaa
            hahmon, jolla on tietty tunnisteluku.

        Args:
            character_id (int): Haetun hahmon tunnisteluku.

        Returns:
            Hahmo-olio, joka on luotu suorittamalla _get_character_by_row
            kyselyn palauttamaan riviin.
        """
        cursor = self._connection.cursor()

        sql = """SELECT character_id, creator_id, name, ancestry, heritage,
                level, experience, hit_points FROM characters
                WHERE character_id=:character_id"""

        cursor.execute(sql, {"character_id": character_id})
        row = cursor.fetchone()

        return _get_character_by_row(row)

    def create(self, character):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka tallettaa
            hahmon taulukkoon.

        Args:
            character (Character): Hahmo-olio, joka talletetaan SQLite-
            tietokantaan.

        Returns:
            Talletettu Hahmo-olio. Oliolta puuttuu SQLitessä sille asetettu
            tunnisteluku.
        """

        cursor = self._connection.cursor()
        sql = """INSERT INTO characters (creator_id, name, ancestry, heritage,
                level, experience, hit_points)
                VALUES (:creator_id, :name, :ancestry, :heritage, :level,
                :experience, :hit_points)"""

        cursor.execute(
            sql, {
                "creator_id": character.creator_id,
                "name": character.name,
                "ancestry": character.ancestry,
                "heritage": character.heritage,
                "level": character.level,
                "experience": character.experience,
                "hit_points": character.hit_points
                })

        self._connection.commit()

        return character

    def delete_character_by_id(self, character_id):
        """Toteuttaa SQL-kyselyn tietokantaan, joka poistaa hahmon jolla on
            annettu tunnisteluku.
        """

        cursor = self._connection.cursor()

        sql = "DELETE FROM characters WHERE character_id=:character_id"

        cursor.execute(sql, {"character_id": character_id})


    def delete_all(self):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka poistaa
            kaikki hahmotaulukon hahmot.
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM characters")

        self._connection.commit()

    def update_character_name(self, character_id, new_name):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka muokkaa
            tietyn hahmon nimisaraketta.

        Args:
            character_id (int): Muokattavan hahmon tunnisteluku.
            new_name (str): Muokattavalle hahmolle asetettava nimi.
        """

        cursor = self._connection.cursor()
        sql = """UPDATE characters SET name=:new_name WHERE character_id=:character_id"""

        cursor.execute(sql, {"new_name": new_name, "character_id": character_id})
        self._connection.commit()

    def update_character_property(self, char_id, target_property, new_value):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka muokkaa
            yhtä tietyn hahmon sarakkeista.

        Ennen kyselyn suorittamista funktio lisää parametrin merkkijonoissa
        mahdollisesti olevien lainausmerkkien eteen kenoviivan, jotta ne
        eivät mahdollistaisi SQL-injektiota.

        Args:
            char_id (int): Muokattavan hahmon tunnisteluku.
            target_property (str): Muokattavan sarakkeen nimi.
            new_value (int): Muokattavan sarakkeen uusi arvo.
        """

        cursor = self._connection.cursor()
        if isinstance(target_property, str):
            target_property.replace("'", "\\'")
            target_property.replace("\"", "\\\"")

        if isinstance(new_value, str):
            new_value.replace("'", "\\'")
            new_value.replace("\"", "\\\"")

        sql = f"""UPDATE characters SET {target_property}=:new_value
                WHERE character_id=:character_id"""

        cursor.execute(sql, {
            "new_value": new_value,
            "character_id": char_id
            })
        self._connection.commit()

character_repository = CharacterRepository(get_database_connection())
