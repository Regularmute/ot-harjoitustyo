class Character:
    """Hahmo-olio jonka avulla käsitellään taulukkoihin meneviä ja sieltä tulevia rivejä.

    Attributes:
        creator_id (int): Hahmon luoneen käyttäjän tunnisteluku.
        name (str): Hahmon nimi.
        ancestry (str): Hahmon syntyperä (esim. ihminen, haltia, tonttu)
        heritage (str): Hahmon "perimä",
            riippuu yleensa syntyperästä (esim. luolahaltia)
        level (int): Hahmon taso. Lähtökohtaisesti 1-20.
        experience (int): Hahmon kokemuspisteet. Johtavat tason nousuun.
        hit_points (int): Hahmon vahinkopisteet.
        character_id (int): Hahmon oma tunnisteluku. Asetetaan SQLitessä.
    """

    def __init__(
        self,
        creator_id,
        name,
        ancestry,
        heritage,
        level,
        experience,
        hit_points,
        character_id=None):

        """Alustaa olion annetuilla parametreilla. Tunnisteluku on None, kunnes se haetaan
            hahmotaulukosta, jossa se on asetettu.
        """

        self.creator_id = creator_id
        self.name = name
        self.ancestry = ancestry
        self.heritage = heritage
        self.level = level
        self.experience = experience
        self.hit_points = hit_points
        self.character_id = character_id
