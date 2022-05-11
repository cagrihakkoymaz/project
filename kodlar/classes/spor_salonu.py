from classes.alet import alet
from classes.kisisel_koc import kisiel_koc
from classes.abone import abone


class spor_salonu(object) :
    def __init__(self,sahibi, butce):
        self.sahibi = sahibi
        self.butce = butce
        self.uyeler = []
        self.koclar = []
        self.aletler = []
        self.paketler =  []
        self.bakim_gerekli_aletler = []
        self.tamir_gerekli_aletler = []

    def bilgileriGoster(self):
        print("Spor Salonu bilgileri gosteriliyor...")
        print("Sahibi: ",self.sahibi) 
        for i in self.paketler:
            print("Paketler: ", i.tur)
        for i in self.uyeler:
            print("Uyeler: ", i.isim)

    def uyeKaydet(self,abone):  
        self.uyeler.append(abone)
        # return yeni_abone

    def kisiselKocKaydet(self,isim,soyisim,uzmanlik_alani):
        yeni_koc = kisiel_koc(isim,soyisim,uzmanlik_alani)
        self.koclar(yeni_koc)
        # return yeni_koc
    
    def aletKaydet(self,alet_ismi, son_bakim_tarihi):
        yeni_alet = alet(alet_ismi,son_bakim_tarihi)
        self.aletler.append(yeni_alet)
