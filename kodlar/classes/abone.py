from classes.kisi import kisi
from classes.saglik_raporu import saglik_raporu

import time
import datetime



class abone(kisi):  # uyelik turunu iptal ettim, bunun yerine kart ekledim 
    def __init__(self,isim,soyisim,paket,ay_sayisi,butce):
        kisi.__init__(self,isim,soyisim)
        self.kart = False  # veznedar saglik belgelerini kabul ettiginde bu degiskeni true yaparak aboneligi baslatir.
        self.saglik_raporlari = []
        self.son_abonelik_tarihi = ""
        self.abonelik_baslangic_tarihi = ""
        self.ay_sayisi = ay_sayisi
        self.butce = butce

        self.abonelik_paketi = paket

    def bilgileriGoster(self):
        kisi.bilgileriGoster(self)
    
        if(self.kart):
            print("Abonelik Turu: ", self.abonelik_paketi.tur)
            print("Abonelik Aktif")
        else :
            print("Abonelik Aktif Değil Lütfen Vezneden Kartinizi Alin")

        for i in range(len(self.saglik_raporlari)):
            print("saglik raporlari: ", self.saglik_raporlari[i].alinma_tarihi )

    def saglikRaporuEkle(self):
        alinma_tarihi = datetime.datetime.now()
        yeni_rapor = saglik_raporu(alinma_tarihi)
        self.saglik_raporlari.append(yeni_rapor)

    def durumKontrolu(self):
        pass
    
    
