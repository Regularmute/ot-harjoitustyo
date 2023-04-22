class Character:
    def __init__(self, creator_id, name, level, experience, hit_points, character_id=None):
        self.creator_id = creator_id
        self.name = name
        self.level = level
        self.experience = experience
        self.hit_points = hit_points
        self.character_id = character_id
