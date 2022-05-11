from classes.spor_salonu import spor_salonu


class abonelik_paketleri(object) :
    def __init__(self, tur, fiyat,gun_sayisi,salon):
        self.tur = tur
        self.fiyat = fiyat 
        self.gun_sayisi = gun_sayisi
        self.salonaEkle(salon)

    def bilgileriGoster(self):
        print("Abonelik paket bilgileri gösteriliyor...")
        print("tur: ",self.tur)
        print("fiyat: ",self.fiyat) 
        print("gun sayisi: ",self.gun_sayisi) 
        print("---------")

    def salonaEkle(self,salon):
        salon.paketler.append(self)
