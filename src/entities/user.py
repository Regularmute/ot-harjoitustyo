class User:

    def __init__(self, username, passwordhash, user_id=None):
        self.username = username
        self.password = passwordhash
        self.user_id = user_id
