class Character:
    """Hahmo-olio jonka avulla käsitellään taulukkoihin meneviä ja sieltä tulevia rivejä.

    Attributes:
        creator_id (int): Hahmon luoneen käyttäjän tunnisteluku.
        name (str): Hahmon nimi.
        level (int): Hahmon taso.
        experience (int): Hahmon kokemuspisteet.
        hit_points (int): Hahmon vahinkopisteet.
        character_id (int): Hahmon oma tunnisteluku. Asetetaan SQLitessä.
    """

    def __init__(self, creator_id, name, level, experience, hit_points, character_id=None):
        """Alustaa olion annetuilla parametreilla. Tunnisteluku on None, kunnes se haetaan
            hahmotaulukosta, jossa se on asetettu.
        """

        self.creator_id = creator_id
        self.name = name
        self.level = level
        self.experience = experience
        self.hit_points = hit_points
        self.character_id = character_id
