import sqlite3
from config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    """Palauta yllä luotu config.py:ssä sijaitsevan tietokantatiedoston ja
    SQLiten välillä oleva yhteys.

    Returns:
        yhteys SQLite-tietokantaan.
    """
    return connection
