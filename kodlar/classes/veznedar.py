from classes.kisi import kisi
from classes.abone import abone
from classes.abonelik_paketleri import abonelik_paketleri
import time

class veznedar(kisi):

    def __init__(self):
        self.gunluk_kasa = 0

    def uyeKaydet(self,abone):

        if(len(abone.saglik_raporlari) != 0 ):
            if( self.ucretAl ):
                abone.kart = True
                abone.abonelik_baslangic_tarihi = time.time()
                self.gunluk_kasa += self.ucretAl(abone)
                print("Kayit Basarili")
            else :
                del abone

        else:
            abone.kart = False
            print("Saglik Raporu Olmadigi icin Kayit Edilemedi")
            del abone
    
    def ucretAl(self,abone):
        if( abone.butce < abone.abonelik_paketi.fiyat * abone.ay_sayisi ):
            return False
        else :
            abone.butce -= abone.abonelik_paketi.fiyat * abone.ay_sayisi
            return abone.abonelik_paketi.fiyat * abone.ay_sayisi

    
