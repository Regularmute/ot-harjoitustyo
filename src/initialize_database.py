from database_connection import get_database_connection


def drop_tables(connection):
    """Poista mahdollisesti olemassaolevat taulukot parametrin tietokannassa."""
    cursor = connection.cursor()

    cursor.executescript('''
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS characters;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo uudet, tyhjät käyttäjä- ja hahmotaulukot parametrin tietokantaan.

    Käyttäjätaulukko pitää kirjaa käyttäjätunnuksista sekä salasanoista (jotka
    hashataan sovelluslogiikan puolella). Lisäksi jokaiselle käyttäjälle asetetaan
    oma ID. Hahmotaulukko ylläpitää hahmon nimen, luoneen käyttäjän ID:n, tason,
    kokemuspisteet ja vahinkopisteet. Lisäksi jokaiselle hahmolle asetetaan oma ID.
    """
    cursor = connection.cursor()

    cursor.executescript('''
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
        CREATE TABLE characters (
            character_id INTEGER PRIMARY KEY,
            creator_id INTEGER REFERENCES users ON DELETE CASCADE,
            name TEXT,
            ancestry TEXT,
            heritage TEXT,
            level INTEGER,
            experience INTEGER,
            hit_points INTEGER
        );
    ''')

    connection.commit()


def initialize_database():
    """Alusta sovelluksen käyttämä tietokanta käyttäjä- ja hahmotaulukoilla.

    Attributes:
        connection: Yhteys käsiteltävään tietokantaan.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
