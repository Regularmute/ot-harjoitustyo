from database_connection import get_database_connection
from entities.character import Character

def get_character_by_row(row):
    return Character(
            row["creator_id"],
            row["name"],
            row["level"],
            row["experience"],
            row["hit_points"],
            row["character_id"]
        ) if row else None

class CharacterRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        # fetch a list of all characters

        cursor = self._connection.cursor()

        cursor.execute("""SELECT character_id, creator_id, name, level, experience,
                        hit_points FROM characters;""")
        rows = cursor.fetchall()

        return list(map(get_character_by_row, rows))

    def get_one_by_name(self, name):
        cursor = self._connection.cursor()

        sql = "SELECT name FROM characters WHERE name = :name"
        cursor.execute(sql, {"name": name})
        row = cursor.fetchone()

        return Character(row["name"], 1, 0, 0, 0) if row else None

    def get_one_by_creator_id(self, creator_id):
        cursor = self._connection.cursor()

        sql = """SELECT character_id, creator_id, name, level, experience, hit_points
                FROM characters WHERE creator_id=:creator_id"""

        cursor.execute(sql, {"creator_id": creator_id})
        row = cursor.fetchone()

        return get_character_by_row(row)

    def create(self, character):
        # store username and hashed password to the database.
        # sqlite adds an autoincrementing Integer for character_id.

        cursor = self._connection.cursor()
        sql = """INSERT INTO characters (creator_id, name, level, experience, hit_points)
                VALUES (:creator_id, :name, :level, :experience, :hit_points)"""

        cursor.execute(
            sql, {
                "creator_id": character.creator_id,
                "name": character.name,
                "level": character.level,
                "experience": character.experience,
                "hit_points": character.hit_points
                })

        self._connection.commit()

        return character

    def delete_all(self):
        # delete all characters from the table

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM characters")

        self._connection.commit()


character_repository = CharacterRepository(get_database_connection())
