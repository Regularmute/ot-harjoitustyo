from database_connection import get_database_connection
from entities.character import Character


class CharacterRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        # fetch a list of all characters

        cursor = self._connection()

        cursor.execute("SELECT name FROM characters;")
        rows = cursor.fetchall()

        return list(map(Character(["name"], 1, 0, 0, 0), rows))

    def get_one_by_name(self, name):
        cursor = self._connection.cursor()

        sql = "SELECT name FROM characters WHERE name = :name"
        cursor.execute(sql, {"name": name})
        row = cursor.fetchone()

        return Character(row["name"], 1, 0, 0, 0) if row else None

    def create(self, character):
        # store username and hashed password to the database

        cursor = self._connection.cursor()
        sql = "INSERT INTO characters (name) VALUES (:name)"

        cursor.execute(
            sql, {"name": character.name})

        self._connection.commit()

        return character


character_repository = CharacterRepository(get_database_connection())
