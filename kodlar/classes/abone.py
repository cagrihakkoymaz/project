from classes.kisi import kisi
from classes.saglik_raporu import saglik_raporu

import datetime
datetime.datetime.now()



class abone(kisi):  # uyelik turunu iptal ettim, bunun yerine status ekledim 
    def __init__(self,isim,soyisim):
        kisi.__init__(self,isim,soyisim)
        self.status = False  # veznedar saglik belgelerini kabul ettiginde bu degiskeni true yaparak aboneligi baslatir.
        self.saglik_raporlari = []
        self.son_abonelik_tarihi

    def bilgileriGoster(self):
        kisi.bilgileriGoster(self)
        print("abone durumu: ", self.status)

    def saglikRaporuEkle(self,alinma_tarihi):
        yeni_rapor = saglik_raporu(alinma_tarihi)
        self.saglik_raporlari.append(yeni_rapor)
    
    
