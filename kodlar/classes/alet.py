import time
class alet(object) :

    def __init__(self,isim, tarih, bakim_maliyeti, tamir_maliyeti,salon):

        self.isim = isim
        self.son_bakim_tarihi = tarih
        self.bakim_gerekli = False
        self.tamir_gerekli = False

        self.bakim_maliyeti = bakim_maliyeti
        self.tamir_maliyeti = tamir_maliyeti
        self.salonaEkle(salon)
        print( self.isim,"aleti salona eklendi")   

    def bilgileriGoster(self):
        print("Alet bilgileri gosteriliyor...")
        print("Alet ismi: ",self.isim) 
        print("son bakim tarihi: ", time.asctime( time.localtime(self.son_bakim_tarihi))) 



    def bakimGoster(self):
        if(time.time() - self.son_bakim_tarihi > 5) : # 6 ay = 15 778 463 saniye
            self.bakim_gerekli = True
            
    
    def tamirGoster(self):
        if(time.time() - self.son_bakim_tarihi > 90000000000 * 2) : # 12 ay = 2 * 15 778 463 saniye
            self.tamir_gerekli = True

    def salonaEkle(self,salon):
        salon.aletler.append(self)
