from database_connection import get_database_connection
import bcrypt
from user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        # fetch a list of all users

        cursor = self._connection()

        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        return list(map(User(["username"],["password"]), rows))

    def create(self, user):
        # convert password to bytes and generate salt for hashing
        byte_password = user.password.encode('utf-8')
        password_salt = bcrypt.gensalt()
        hash_value = bcrypt.hashpw(byte_password, password_salt)

        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"

        cursor.execute(sql, {"username": user.username, "password":hash_value})

        self._connection.commit()

        return user

user_repository = UserRepository(get_database_connection())