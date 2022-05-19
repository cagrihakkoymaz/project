from classes.kisi import kisi

class salon_yoneticisi(kisi):
    def __init__(self,isim,soyisim):
        kisi.__init__(self,isim,soyisim)

        print( self.isim,self.soyisim,"salon yoneticisi olarak atandi")
    def salonButceGoruntule(self,salon):
        print("Salonun kasasında bulunan tutar : ",salon.butce)

