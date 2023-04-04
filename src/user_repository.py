from database_connection import get_database_connection
import bcrypt
class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, username, password):
        # convert password to bytes and generate salt for hashing
        byte_password = password.encode('utf-8')
        password_salt = bcrypt.gensalt()
        hash_value = bcrypt.hashpw(byte_password, password_salt)

        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"

        cursor.execute(sql, {"username": username, "password":hash_value})

        self._connection.commit()

        return username

user_repository = UserRepository(get_database_connection())