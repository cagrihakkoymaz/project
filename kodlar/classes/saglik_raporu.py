class saglik_raporu(object) :
    def __init__(self,alinma_tarihi):
        self.alinma_tarihi = alinma_tarihi
        

    def bilgileriGoster(self):
        print("alinma tarihi gosteriliyor...")
        print("Alinma Tarihi: ",self.alinma_tarihi) 


