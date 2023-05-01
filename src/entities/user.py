class User:
    """Käyttäjä-olio jonka avulla käsitellään taulukkoihin meneviä ja sieltä tulevia rivejä.

        Attributes:
            username (str): Käyttäjän tunnus.
            password (str): Käyttäjän salasana. Hashattu sovelluslogiikan puolella.
            user_id (str): Käyttäjän identifioiva tunnistenumero. Asetetaan SQLitessä.
    """

    def __init__(self, username, passwordhash, user_id=None):
        """Alustaa olion annetuilla parametreillä. User_id on tyhjä,
            kunnes se haetaan taulukosta jossa se on asetettu.
        """

        self.username = username
        self.password = passwordhash
        self.user_id = user_id
