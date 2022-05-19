import unittest
import time

from classes.kisi import kisi
from classes.kisisel_koc import kisiel_koc
from classes.abone import abone
from classes.veznedar import veznedar
from classes.spor_salonu import spor_salonu
from classes.alet import alet
from classes.salon_yoneticisi import salon_yoneticisi
from classes.abonelik_paketleri import abonelik_paketleri
from classes.saglik_raporu import saglik_raporu


start_time = time.time()

spor_salonu_obj= spor_salonu("Spor Salonu", 10000)
salon_yoneticisi_obj = salon_yoneticisi("Salon", "Yoneticisi")

kisi = kisi('Deneme','Kisisi')
koc = kisiel_koc('Deneme','Kocu','Alan1')

#abonelik_paketleri("standart",500,5, spor_salonu_obj)
#abonelik_paketleri("baslangic",300,3, spor_salonu_obj)
#abonelik_paketleri("premium",1000,7, spor_salonu_obj)

standart_paket = abonelik_paketleri("standart",500,5, spor_salonu_obj)
baslangic_paket = abonelik_paketleri("baslangic",300,3, spor_salonu_obj)
premium_paket = abonelik_paketleri("premium",1000,7, spor_salonu_obj)

dumble = alet("dumble",time.time()-432000,100,1000, spor_salonu_obj)
halter = alet("halter",time.time()-86400,1000,100000, spor_salonu_obj)
kosu_bandi = alet("kosu_bandi",time.time(),10,20, spor_salonu_obj)

veznedar = veznedar()

abone1 = abone("Abone","Bir",5000)
abone2 = abone("Abone","Iki",50)

abone1.saglikRaporuEkle()
abone2.saglikRaporuEkle()


veznedar.uyeKaydet(abone1,spor_salonu_obj) 
veznedar.uyeKaydet(abone2,spor_salonu_obj)


class unitTest(unittest.TestCase):

    def test_ucretAl(self):
        self.assertEqual(veznedar.ucretAl(abone1), 1500)

    def test_ucretYetersiz(self):
        self.assertEqual(veznedar.ucretAl(abone2), False)

    def test_abonelik_paketleri(self):
        self.assertEqual(standart_paket.tur, 'standart')
        self.assertEqual(standart_paket.fiyat, 500)
        self.assertEqual(standart_paket.gun_sayisi, 5)

        self.assertEqual(baslangic_paket.tur, 'baslangic')
        self.assertEqual(baslangic_paket.fiyat, 300)
        self.assertEqual(baslangic_paket.gun_sayisi, 3)

        self.assertEqual(premium_paket.tur, 'premium')
        self.assertEqual(premium_paket.fiyat, 1000)
        self.assertEqual(premium_paket.gun_sayisi, 7)

    def test_alet(self):
        self.assertEqual(dumble.isim, 'dumble')
        self.assertTrue(dumble.son_bakim_tarihi,time.time()-432000<10)
        self.assertEqual(dumble.bakim_maliyeti, 100)
        self.assertEqual(dumble.tamir_maliyeti, 1000)
        self.assertFalse(dumble.bakim_gerekli)
        self.assertFalse(dumble.tamir_gerekli)
        
    def test_kisi(self):
        self.assertEqual(kisi.isim, 'Deneme')
        self.assertEqual(kisi.soyisim, 'Kisisi')
        
    def test_kisiel_koc(self):
        self.assertEqual(koc.isim, 'Deneme')
        self.assertEqual(koc.soyisim, 'Kocu')
        self.assertEqual(koc.uzmanlik_alani, 'Alan1')
        
    def test_spor_salonu(self):
        self.assertEqual(spor_salonu_obj.isim, 'Spor Salonu')
        self.assertEqual(spor_salonu_obj.butce, 10000)
        #self.assertEqual(spor_salonu_obj.uyeler, [abone1, abone2])
        #self.assertEqual(spor_salonu_obj.koclar, [koc])
        #self.assertEqual(spor_salonu_obj.aletler, [dumble, halter, kosu_bandi])
        #self.assertEqual(spor_salonu_obj.paketler, [standart_paket, baslangic_paket, premium_paket])

    def test_saglik_raporu(self):
        self.assertEqual(saglik_raporu('01.01.2022').alinma_tarihi, '01.01.2022')

    def test_paketSun(self):
        self.assertEqual(veznedar.paketSun(abone1,spor_salonu_obj)[0].tur, 'standart')
        self.assertEqual(veznedar.paketSun(abone1,spor_salonu_obj)[1], '5')

    def test_paketSunIptal(self):
        self.assertEqual(veznedar.paketSun(abone1,spor_salonu_obj)[0], -1)
        self.assertEqual(veznedar.paketSun(abone1,spor_salonu_obj)[1], -1)
        

if __name__ == '__main__':
    unittest.main()

