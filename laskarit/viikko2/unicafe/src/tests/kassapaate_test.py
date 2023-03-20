import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_rahat_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)