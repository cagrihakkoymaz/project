from classes.kisi import kisi
from classes.abone import abone
from classes.abonelik_paketleri import abonelik_paketleri
from classes.spor_salonu import spor_salonu
from classes.salon_yoneticisi import salon_yoneticisi


import time

class veznedar(kisi):

    def __init__(self):
        self.gunluk_kasa = 0

    def uyeKaydet(self,abone,salon):
        if(len(abone.saglik_raporlari) != 0 ):
            secilen_paket, ay_sayisi = self.paketSun(abone,salon)
            abone.abonelik_paketi = secilen_paket
            abone.ay_sayisi = int(ay_sayisi)
            abone.abonelik_baslangic_tarihi = time.time()
            if not (secilen_paket == -1 or ay_sayisi == -1):
                if( self.ucretAl(abone)):
                    abone.kart = True

                    self.gunluk_kasa += self.ucretAl(abone)
                    print("Gunluk kasada bulunan guncel miktar :",self.gunluk_kasa)
                    salon.uyeKaydet(abone)
                    print("Kayit Basarili")
                    
                else :
                    print("Butce Yetersiz")
                    del abone

        else:
            abone.kart = False
            print("Saglik Raporu Olmadigi icin Kayit Edilemedi")
            
            del abone
    
    def ucretAl(self,abone):
        if( abone.butce < abone.abonelik_paketi.fiyat * abone.ay_sayisi ):
            return False
        else :
            abone.butce -= abone.abonelik_paketi.fiyat * abone.ay_sayisi
            return abone.abonelik_paketi.fiyat * abone.ay_sayisi

    def paketSun(self,abone,salon):
        for i in salon.paketler:
            i.bilgileriGoster()

        paket = input("Paket Seciniz ")
        ay = input("Kac ay kayit olmak istediginizi girin: ")
        
        for i in salon.paketler:
            if( paket == i.tur and ay != "q") :
                print("secilen paket turu :", paket )
                return i, ay
            elif(paket=="q" or ay == "q"):
                print("Uyelik islemi iptal edildi")

                return -1, -1
        
        print("Gecerli Bir Paket Giriniz iptal için q'ya basiniz: ")

        self.paketSun(abone,salon)

        return -1 -1
    
    def aletDurumSorgula(self, salon, alet,salon_yoneticisi):
        alet.bakimGoster()
        alet.tamirGoster()
        if(alet.tamir_gerekli):
            salon.tamir_gerekli_aletler.append(alet)
        elif(alet.bakim_gerekli):
            salon.bakim_gerekli_aletler.append(alet)

        if(len(salon.bakim_gerekli_aletler) != 0 or len(salon.tamir_gerekli_aletler) != 0):
            print("tamiri ve bakimi gelen aletler")
        else:
            print("Bakim veya Tamir gerektiren alet yoktur")
        for alet in salon.bakim_gerekli_aletler:
            if (alet.bakim_gerekli):
                print(len(salon.bakim_gerekli_aletler))

                print(alet.isim," aletinin bakim talebi ilgili ekiplere otomatik olarak iletilmistir")
                salon.butce-=alet.bakim_maliyeti
                salon.bakim_gerekli_aletler.remove(alet)
                alet.son_bakim_tarihi=time.time()
                alet.bakim_gerekli=False



        for alet in salon.tamir_gerekli_aletler:

            if (alet.tamir_gerekli):
                print(alet.isim," aletinin tamir talebi ilgili ekiplere otomatik olarak iletilmistir")
                salon.butce-=alet.tamir_maliyeti
                salon.tamir_gerekli_aletler.remove(alet)
                alet.son_bakim_tarihi=time.time()
                alet.tamir_gerekli=False











        


    
