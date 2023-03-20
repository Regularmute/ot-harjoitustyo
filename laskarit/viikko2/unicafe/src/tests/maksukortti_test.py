import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_kasvattaa_kortin_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 30.00 euroa")

    def test_ota_rahaa_vahentaa_saldoa_oikein_jos_saldoa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(750)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2.50 euroa")

    def test_ota_rahaa_ei_muuta_saldoa_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_True_jos_rahat_riittivat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(750), True)

    def test_ota_rahaa_palauttaa_False_jos_rahat_eivat_riittaneet(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
