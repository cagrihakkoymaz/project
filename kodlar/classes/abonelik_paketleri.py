class abonelik_paketleri(object) :
    def __init__(self, tur, fiyat):
        self.tur = tur
        self.fiyat = fiyat

    def bilgileriGoster(self):
        print("Abonelik paket bilgileri gösteriliyor...")
        print("tur: ",self.tur)
        print("fiyat: ",self.fiyat) 
