"""Käyttäjä-olioiden sovelluslogiikka.

Käyttää ulkopuolista kirjastoa bcrypt, jonka avulla salataan salasanat ennen tietokantaan
tallentamista, ja verrataan salasanaa taulukon salattua versioon. Kutsuu user_repository.py:tä
tietokannan käsittelemistä varten.
"""

import bcrypt
from repositories.user_repository import (
    user_repository as default_user_repository
)
from entities.user import User


class InvalidCredentialsError(Exception):
    """Väärä käyttäjätunnus tai salasana."""


class UsernameExistsError(Exception):
    """Käyttäjätunnus on jo toisen käyttämä."""


class UserService:
    def __init__(
        self,
        user_repository=default_user_repository
    ):

        self._user_repository = user_repository
        self._user = None

    def create_user(self, username, password, login=True):
        """Rekisteröi uuden käyttäjän tietokantaan.

        Args:
            username (str): uuden käyttäjän käyttäjätunnus. Jos tietokannasta
                löytyy saman tunnuksen omistava käyttäjä, heitetään virhe.
            password (str): uuden käyttäjän salasana. Salataan ennen
                tietokannalle lähettämistä.
            login (bool): arvo, joka määrittää kirjataanko rekisteröity
                käyttäjä sisään. Pääasiassa testausta varten.

        Returns:
            Rekisteröity käyttäjäolio ilman sen tunnistelukua.
        """

        duplicate_username = self._user_repository.get_one_by_username(
            username)

        if duplicate_username:
            raise UsernameExistsError(f"Username {username} is already taken")

        byte_password = password.encode('utf-8')
        password_salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(byte_password, password_salt)

        user = self._user_repository.create(User(username, password_hash))

        if login:
            self._user = user

        return user

    def get_users(self):
        """Hakee tietokannasta kaikki käyttäjät.

        Returns:
            Lista jokaisen tietokannan rivin tiedoista muodostetuista
            käyttäjäolioista.
        """

        return self._user_repository.get_all()

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjäolion."""

        return self._user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Kirjautumiseen käytettyä tunnusta ja salasanaan verrataan tietokantaan
        ja heitetään virhe jos tunnusta ei löydy, tai salasana ei vastaa
        tunnukseen talletettua salattua salasanaa.

        Args:
            username (str): Kirjautumisnäkymään kirjoitettu käyttäjätunnus,
                jota verrataan tietokannassa oleviin käyttäjiin.
            password (str): Kirjautumiseen käytetty salasana, joka enkoodataan
                utf-8 muotoon, ja verrataan bcryptin avulla tietokantaan
                talletetun käyttäjän hashattuun salasanaan.

        Returns:
            Kirjautunut käyttäjäolio, mukaan lukien käyttäjän tunnisteluku.
        """

        byte_password = password.encode('utf-8')
        user = self._user_repository.get_one_by_username(username)

        if not user or not bcrypt.checkpw(byte_password, user.password):
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self._user = None


user_service = UserService()
