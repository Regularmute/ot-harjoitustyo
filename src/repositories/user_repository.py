"""Tietokannan käyttäjätaulukon käsittelylogiikka."""

from database_connection import get_database_connection
from entities.user import User


def _get_user_by_row(row):
    """Luo käyttäjä-olion SQLitestä haetusta rivistä. Helpottaa muun
    sovelluksen toimintaa.

    Args:
        row: Halutun käyttäjän rivi käyttäjätaulukosta. Funktio olettaa, että
        rivi sisältää sarakkeet "username", "password" ja "user_id".

    Returns:
        Käyttäjä-olio, jolle annetaan parametreiksi taulukkorivin sarakkeiden
        arvot. None jos funktio kutsuttiin ilman riviä.
    """

    return User(
            row["username"],
            row["password"],
            row["user_id"]
        ) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka palauttaa
        listan kaikista käyttäjistä.

        Returns:
            Lista käyttäjä-olioista, jotka on luotu suorittamalla
            _get_user_by_row jokaiseen kyselyn palauttamaan riviin.
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT user_id, username, password FROM users;")
        rows = cursor.fetchall()

        return list(map(_get_user_by_row, rows))

    def get_one_by_username(self, username):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka palauttaa
        käyttäjän, jolla on tietty käyttäjätunnus.

        Args:
            username (str): Haetun käyttäjän käyttäjätunnus.

        Returns:
            Käyttäjä-olio, joka on luotu suorittamalla _get_user_by_row
            kyselyn palauttamaan riviin.
        """

        cursor = self._connection.cursor()

        sql = """SELECT user_id, username, password FROM users
                 WHERE username = :username"""
        cursor.execute(sql, {"username": username})
        row = cursor.fetchone()

        return _get_user_by_row(row)

    def create(self, user):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka tallettaa
        käyttäjän taulukkoon.

        Args:
            user (User): Käyttäjäolio, joka talletetaan SQLite-tietokantaan.

        Returns:
            Talletettu käyttäjäolio. Oliolta puuttuu SQLitessä sille asetettu
            tunnisteluku.
        """

        cursor = self._connection.cursor()
        sql = """INSERT INTO users (username, password)
                 VALUES (:username, :password)"""

        cursor.execute(
            sql, {"username": user.username, "password": user.password})

        self._connection.commit()

        return user

    def delete_all(self):
        """Toteuttaa SQL-kyselyn yhdistettyyn tietokantaan, joka poistaa
        kaikki käyttäjätaulukon käyttäjät."""

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
