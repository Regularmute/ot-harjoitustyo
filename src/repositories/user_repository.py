from database_connection import get_database_connection
from entities.user import User

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        # fetch a list of all users

        cursor = self._connection.cursor()

        cursor.execute("SELECT username, password FROM users;")
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def get_one_by_username(self, username):
        cursor = self._connection.cursor()

        sql = "SELECT username, password FROM users WHERE username = :username"
        cursor.execute(sql, {"username": username})
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        # store username and hashed password to the database

        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"

        cursor.execute(
            sql, {"username": user.username, "password": user.password})

        self._connection.commit()

        return user


user_repository = UserRepository(get_database_connection())
