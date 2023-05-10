import unittest
from repositories.character_repository import character_repository
from entities.character import Character


class TestCharacterRepository(unittest.TestCase):
    def setUp(self):
        character_repository.delete_all()
        self.character_drago = Character(
            333,"Drago Mastermind", "human", "skilled", 5, 500, 60)
        self.character_griselda = Character(
            8241, "Earth Mage Griselda", "Elf", "Cavern Elf", 7, 200, 58)
        self.character_blossom = Character(
            8241, "Blossom", "Sylph", "-", 2, 300, 17)

    def characters_are_the_same(self, character1, character2):
        return (character1.creator_id == character2.creator_id
                and character1.name == character2.name
                and character1.ancestry == character2.ancestry
                and character1.heritage == character2.heritage
                and character1.level == character2.level
                and character1.experience == character2.experience
                and character1.hit_points == character2.hit_points)


    def test_create_stores_character_object_correctly(self):
        character_repository.create(self.character_drago)
        characters = character_repository.get_all()

        self.assertEqual(len(characters), 1)
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )
        self.assertEqual(characters[0].character_id, 1)

    def test_get_all_returns_character_objects_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)
        characters = character_repository.get_all()

        self.assertEqual(len(characters), 2)

        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )
        self.assertEqual(characters[0].character_id, 1)

        self.assertTrue(
            self.characters_are_the_same(characters[1], self.character_griselda)
        )
        self.assertEqual(characters[1].character_id, 2)

    def test_get_all_by_creator_id_gets_correct_characters(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)
        character_repository.create(self.character_blossom)

        user_id = self.character_griselda.creator_id
        characters = character_repository.get_all_by_creator_id(user_id)

        self.assertEqual(len(characters), 2)
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_griselda),
            self.characters_are_the_same(characters[1], self.character_blossom)
        )


    def test_delete_all_empties_table_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_repository.delete_all()
        characters = character_repository.get_all()
        self.assertEqual(len(characters), 0)

    def test_get_one_by_character_id_gets_correct_character(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_id_drago = 1
        fetched_character = character_repository.get_one_by_character_id(character_id_drago)

        self.assertTrue(
            self.characters_are_the_same(fetched_character, self.character_drago)
        )
        self.assertEqual(fetched_character.character_id, 1)

    def test_update_character_column_changes_name_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_repository.update_character_column(1, "name", "Khal Drogo")
        characters = character_repository.get_all()

        self.assertEqual(characters[0].name, "Khal Drogo")

        # check other properties are unaffected
        self.assertEqual(characters[0].character_id, 1)
        self.assertEqual(characters[0].creator_id, self.character_drago.creator_id)
        self.assertEqual(characters[0].level, self.character_drago.level)
        self.assertEqual(characters[0].experience, self.character_drago.experience)
        self.assertEqual(characters[0].hit_points, self.character_drago.hit_points)

        # check other characters are unaffected
        self.assertTrue(
            self.characters_are_the_same(characters[1], self.character_griselda)
        )

    def test_update_character_column_updates_level_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_repository.update_character_column(2, "level", 4)
        characters = character_repository.get_all()

        self.assertEqual(characters[1].level, 4)

        # check other properties are unaffected
        self.assertEqual(characters[1].character_id, 2)
        self.assertEqual(characters[1].creator_id, self.character_griselda.creator_id)
        self.assertEqual(characters[1].name, self.character_griselda.name)
        self.assertEqual(characters[1].experience, self.character_griselda.experience)
        self.assertEqual(characters[1].hit_points, self.character_griselda.hit_points)

        # check other characters are unaffected
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )

    def test_update_character_column_updates_experience_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_repository.update_character_column(2, "experience", 350)
        characters = character_repository.get_all()

        self.assertEqual(characters[1].experience, 350)

        # check other properties are unaffected
        self.assertEqual(characters[1].character_id, 2)
        self.assertEqual(characters[1].creator_id, self.character_griselda.creator_id)
        self.assertEqual(characters[1].name, self.character_griselda.name)
        self.assertEqual(characters[1].level, self.character_griselda.level)
        self.assertEqual(characters[1].hit_points, self.character_griselda.hit_points)

        # check other characters are unaffected
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )

    def test_update_character_column_updates_hp_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        character_repository.update_character_column(2, "hit_points", 61)
        characters = character_repository.get_all()

        self.assertEqual(characters[1].hit_points, 61)

        # check other properties are unaffected
        self.assertEqual(characters[1].character_id, 2)
        self.assertEqual(characters[1].creator_id, self.character_griselda.creator_id)
        self.assertEqual(characters[1].name, self.character_griselda.name)
        self.assertEqual(characters[1].level, self.character_griselda.level)
        self.assertEqual(characters[1].experience, self.character_griselda.experience)

        # check other characters are unaffected
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )

    def test_delete_character_by_id_works_correctly(self):
        character_repository.create(self.character_drago)
        character_repository.create(self.character_griselda)

        characters = character_repository.get_all()
        self.assertEqual(len(characters), 2)
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_drago)
        )

        character_repository.delete_character_by_id(1)
        characters = character_repository.get_all()

        self.assertEqual(len(characters), 1)
        self.assertTrue(
            self.characters_are_the_same(characters[0], self.character_griselda)
        )
