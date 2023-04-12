from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.executescript('''
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS characters;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.executescript('''
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
        CREATE TABLE characters (
            character_id INTEGER PRIMARY KEY,
            name TEXT,
            level INTEGER,
            experience INTEGER,
            hit_points INTEGER,
            proficiency bonus INTEGER
        );
        INSERT INTO characters (name)
        VALUES ("gamerGUY");
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
