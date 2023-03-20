import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahat_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_edulliset_myynnit_ovat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_maukkaat_myynnit_ovat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_nostaa_rahamaaraa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_palauttaa_vaihtorahan_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_syo_edullisesti_kateisella_nostaa_edullisten_myynnit_oikein(self):
        edulliset_myynnit_alussa = self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, edulliset_myynnit_alussa + 1)

    def test_syo_edullisesti_kateisella_ei_nosta_kassassa_rahaa_jos_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_palauttaa_koko_maksun_jos_maksu_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(210), 210)

    def test_syo_edullisesti_kateisella_ei_nosta_myynteja_jos_maksu_ei_riita(self):
        edulliset_myynnit_alussa = self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, edulliset_myynnit_alussa)

    def test_syo_maukkaasti_kateisella_nostaa_rahamaaraa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_palauttaa_vaihtorahan_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_syo_maukkaasti_kateisella_nostaa_maukkaat_myynnit_oikein(self):
        maukkaat_myynnit_alussa = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, maukkaat_myynnit_alussa + 1)

    def test_syo_maukkaasti_kateisella_ei_nosta_kassassa_rahaa_jos_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_palauttaa_koko_maksun_jos_maksu_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_syo_maukkaasti_kateisella_ei_nosta_myynteja_jos_maksu_ei_riita(self):
        maukkaat_myynnit_alussa = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, maukkaat_myynnit_alussa)

# Korttiostot