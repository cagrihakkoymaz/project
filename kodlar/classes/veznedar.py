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
                    print("-------------------------------")

                    print("|| Butce Yetersiz,  Kayit Basarisiz ||")
                    print("-------------------------------")

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
        print("-----------------------------------------------------------------------------------------------------------")
        print("||  !!!! Gecerli Bir Paket Giriniz iptal için q'ya basiniz, Gecerli Paketler Assagida Gosterilmektedir !!!  ||\n ")
        print("-----------------------------------------------------------------------------------------------------------")


        self.paketSun(abone,salon)

        return -1 -1
    
    def aletDurumSorgula(self, salon):

        for alet in salon.aletler:
            alet.bakimGoster()
            alet.tamirGoster()
            if(alet.tamir_gerekli):
                salon.tamir_gerekli_aletler.append(alet)
            elif(alet.bakim_gerekli):
                salon.bakim_gerekli_aletler.append(alet)

        for alet in salon.bakim_gerekli_aletler:
            if (alet.bakim_gerekli):
                print(len(salon.bakim_gerekli_aletler))

                print(alet.isim," aletinin bakim talebi ilgili ekiplere otomatik olarak iletilmistir")

                if(salon.butce < alet.bakim_maliyeti) :
                    print(alet.isim,"ALETI ICIN BUTCE YETERSIZ, BAKIM YAPILAMADI")
                    salon.bakim_gerekli_aletler.remove(alet)
                else :
                    salon.butce-=alet.bakim_maliyeti
                    
                    salon.bakim_gerekli_aletler.remove(alet)
                    alet.son_bakim_tarihi=time.time()
                    alet.bakim_gerekli=False



        for alet in salon.tamir_gerekli_aletler:

            if (alet.tamir_gerekli):
                print(alet.isim," aletinin tamir talebi ilgili ekiplere otomatik olarak iletilmistir")
                if(salon.butce < alet.tamir_maliyeti) :
                    print(alet.isim, "ALETİ ICIN BUTCE YETERSIZ, TAMİR YAPILAMADI")
                    salon.tamir_gerekli_aletler.remove(alet)
                else :                
                    salon.butce-=alet.tamir_maliyeti
                    salon.tamir_gerekli_aletler.remove(alet)
                    alet.son_bakim_tarihi=time.time()
                    alet.tamir_gerekli=False



    def saglikRaporSorgula(self, salon):
        silinecek_uyeler = []
        for uye in salon.uyeler:
        

            print("saglik raporlari: ",  time.asctime( time.localtime(uye.saglik_raporlari[-1].alinma_tarihi )))
            if(time.time() - uye.saglik_raporlari[-1].alinma_tarihi > 20) : # 6 ay = 15 778 463 saniye

                print("SAglik raporu sure asimi!!! Yeni saglik raporu gerekli")

                saglik_raporu = input("Aile Hekiminizden yeni saglik raporu almak icin e'ye basiniz, \nalmak istemiyorsunuz e disinda bir tusa basin ")
    
                if( saglik_raporu == 'e') :
                    print("Yeni Saglik Raporu Alindi")
                    uye.saglikRaporuEkle()
                else :
                    silinecek_uyeler.append(uye)
                return silinecek_uyeler
                        










        


    
