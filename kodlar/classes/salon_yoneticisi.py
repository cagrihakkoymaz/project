from classes.kisi import kisi

class salon_yoneticisi(kisi):
    def __init__(self,isim,soyisim,salon_kapital):
        kisi.__init__(self,isim,soyisim)
        self.salon_kapital = salon_kapital
