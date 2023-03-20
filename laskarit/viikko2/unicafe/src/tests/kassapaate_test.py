import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.koyha_kortti = Maksukortti(20)

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
# Onnistuneet ostokset, kun kortilla on tarpeeksi rahaa
    def test_syo_edullisesti_kortilla_vahentaa_kortin_saldoa_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_edullisesti_kortilla_palauttaa_true_jos_kortilla_on_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kortilla_nostaa_edullisten_myynnit_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_vahentaa_kortin_saldoa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_palauttaa_true_jos_kortilla_on_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_nostaa_edullisten_myynnit_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

# Epäonnistuneet ostokset, kun kortilla ei ole tarpeeksi rahaa

    def test_syo_edullisesti_kortilla_ei_vahenna_kortin_saldoa_jos_saldo_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyha_kortti)

        self.assertEqual(self.koyha_kortti.saldo, 20)

    def test_syo_edullisesti_kortilla_palauttaa_false_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.koyha_kortti), False)

    def test_syo_edullisesti_kortilla_ei_nosta_edullisten_myynteja_jos_saldo_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyha_kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kortilla_ei_muuta_kassan_rahamaaraa_vaikka_saldo_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_ei_vahenna_kortin_saldoa_jos_saldo_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyha_kortti)

        self.assertEqual(self.koyha_kortti.saldo, 20)

    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.koyha_kortti), False)

    def test_syo_maukkaasti_kortilla_ei_nosta_maukkaiden_myynteja_jos_saldo_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyha_kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_ei_muuta_kassan_rahamaaraa_vaikka_saldo_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

# Kortin saldon lataus

    def test_lataa_rahaa_kortille_nostaa_kortin_saldoa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2000)
        self.assertEqual(self.maksukortti.saldo, 3000)

    def test_lataa_rahaa_kortille_nostaa_kassan_rahamaaraa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 102000)