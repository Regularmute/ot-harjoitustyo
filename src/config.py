"""Moduuli joka lukee ympäristömuuttujien arvot sovellukselle.

Tämä moduuli lukee dotenv-kirjaston avulla tiedoston src/.env sisältämät
ympäristömuuttujat, ja asettavat ne omiin muuttujiinsa, joita muut moduulit
voivat kutsua.

Attributes:
    DATABASE_FILENAME (str): Sovelluksen tietokantatiedoston nimi. Jos
        ympäristömuuttujaa ei ole, aseta nimeksi "database.sqlite".
    DATABASE_FILE_PATH (str): Tietokantatiedoston sijainti; polku
        src/data/(DATABASE_FILENAME).
"""

import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
