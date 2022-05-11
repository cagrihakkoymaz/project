class kisi(object) :
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def bilgileriGoster(self):
        print("Kisi bilgileri gosteriliyor...")
        print("İsim: ",self.isim,"\nsoyisim: ",self.soyisim) 


# class abone(kisi):
#     def __init__(self,isim,soyisim,uyelik_turu):
#         print("Abone yaratılıyor")
#         kisi.__init__(self,isim,soyisim)
#         self.uyelik_turu = uyelik_turu

    

# abone1 = abone("alpis","pisko","5")
# abone1.bilgileriGoster()

