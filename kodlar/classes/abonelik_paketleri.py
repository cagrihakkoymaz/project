class abonelik_paketleri(object) :
    def __init__(self, tur, fiyat,gun_sayisi):
        self.tur = tur
        self.fiyat = fiyat 
        self.gun_sayisi = gun_sayisi

    def bilgileriGoster(self):
        print("Abonelik paket bilgileri gösteriliyor...")
        print("tur: ",self.tur)
        print("fiyat: ",self.fiyat) 
