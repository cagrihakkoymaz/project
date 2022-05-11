from classes.kisi import kisi

class kisiel_koc(kisi):
    def __init__(self,isim,soyisim,uzmanlik_alani):
        kisi.__init__(self,isim,soyisim)
        self.uzmanlik_alani = uzmanlik_alani

    def bilgileriGoster(self):
        kisi.bilgileriGoster(self)
        print("uzmanlik alani: ", self.uzmanlik_alani)

    