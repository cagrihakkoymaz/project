# from kisi import *
from faulthandler import dump_traceback_later
from classes.kisi import kisi

# from abone import *
from classes.kisisel_koc import kisiel_koc
from classes.abone import abone
from classes.veznedar import veznedar
from classes.spor_salonu import spor_salonu
from classes.alet import alet
from classes.salon_yoneticisi import salon_yoneticisi


import datetime
import time

from classes.abonelik_paketleri import abonelik_paketleri


 ## TODO 
 ## - butce planlaması icin guncel uyelerle 1 yillik sonunda ek gelir gider olusturulabilir
 ## - saglik raporlari 1 yilin sonunda sistemden dusecek, onun kontrolu yapilacak
 ## - tamir bakim maliyeti sorgulama
 ## - 
""" 
alperen_spor_salonu = spor_salonu("Alp",500)

standart_paket = abonelik_paketleri("standart",500,5, alperen_spor_salonu)
baslangic_paket = abonelik_paketleri("baslangic",300,3, alperen_spor_salonu)
premium_paket = abonelik_paketleri("premium",1000,7, alperen_spor_salonu)



#alperen_spor_salonu.bilgileriGoster()


cagri = abone("cagri","Hakkoymaz",58)
veznedar = veznedar()

veznedar.uyeKaydet(cagri,alperen_spor_salonu)  
print("*--------------")



cagri.saglikRaporuEkle()


veznedar.uyeKaydet(cagri,alperen_spor_salonu)  


# print("SANİYE",time.time())
# print(time.asctime( time.localtime(time.time()) ))


# dumble=alet(20,5,dumble)



#print("*--------------")
#cagri.bilgileriGoster()

#print("SALONN")
#alperen_spor_salonu.bilgileriGoster()

#print("/////////////////////---------------------\\\\\\\\\\\\\\\\")
salon_yoneticisi = salon_yoneticisi("Enes", "Dilsiz",50000)
dumble = alet("dumble",time.time() - 150000,500,2000)
dumble.bilgileriGoster()
b = input("bekleme")

veznedar.aletDurumSorgula(alperen_spor_salonu, dumble,salon_yoneticisi)

dumble.bilgileriGoster()

b = input("bekleme")

veznedar.aletDurumSorgula(alperen_spor_salonu, dumble,salon_yoneticisi)

dumble.bilgileriGoster()
 """
print("""*******************

FIT AND HIT

İşlemler ;

1. SPOR SALONU KAYDET

2.SALON YONETICISI KAYDET

3. YENİ PAKET TANIMLA

4. SALON BİLGİLERİNİ GOSTER

5. ALET KAYDET

6. UYE KAYDET

7. ALET DURUM SORGULA

8.GUNLUK KASAYI SALON_KASAYA AKTAR

9:SALON KASAYI GUNLUK KASAYA AKTAR

Çıkmak için 'q' ya basın.
*******************""")
"""
isim = input("Salon ismini giriniz ")
kasa= input("Salon butcesini sayi olarak giriniz ")
try:
    kasa=int(kasa)
    spor_salonu_obj = spor_salonu(isim,kasa)

except:
    print("Lutfen butceyi sayi giriniz")

isim = input("Salon yoneticisinin ismini giriniz ")
soyisim= input("Salon yoneticisin soyismini giriniz ")
salon_yoneticisi_obj = salon_yoneticisi(isim, soyisim)
"""

start_time = time.time()

spor_salonu_obj = spor_salonu("Alperen",10000)
salon_yoneticisi_obj = salon_yoneticisi("enes","dilsiz")
veznedar = veznedar()

abonelik_paketleri("standart",500,5, spor_salonu_obj)
abonelik_paketleri("baslangic",300,3, spor_salonu_obj)
abonelik_paketleri("premium",1000,7, spor_salonu_obj)

alet("dumble",time.time()-432000,100,1000, spor_salonu_obj)
alet("halter",time.time()-86400,1000,100000, spor_salonu_obj )
alet("kosu_bandi",time.time(),10,20, spor_salonu_obj)



while True:
    print("""*******************

    FIT AND HIT

    İşlemler ;

    1. SPOR SALONU KAYDET

    2.SALON YONETICISI KAYDET

    3. YENİ PAKET TANIMLA

    4. SALON BİLGİLERİNİ GOSTER

    5. ALET KAYDET

    6. UYE KAYDET

    7. ALET DURUM SORGULA

    8.GUNLUK KASAYI SALON_KASAYA AKTAR

    9.SALON KASAYI GUNLUK KASAYA AKTAR

    10. GUNLUK KASA TUTARI

    11. SALON KASA TUTARI

    12. SAGLIK RAPORU SORGULA

    Çıkmak için 'q' ya basın.
    *******************""")
    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        break

    if (işlem == "3"):
        abonelik_paket_ismi = input("Paket Ismi Giriniz: ")
        paket_fiyati = input("Paket Fiyatini sayi olarak giriniz")
        gun= input("Gün sayisini sayi olarak giriniz ")
        try:
            gun=int(gun)
            paket_fiyati = int(paket_fiyati)
            abonelik_paketleri(abonelik_paket_ismi,paket_fiyati, gun,spor_salonu_obj)

        except:

            print("Lutfen sayi olarak giris yapiniz")

        # a = abonelik_paketleri("standart",500,5, spor_salonu_obj)  
        # b = abonelik_paketleri("asd",100,3,spor_salonu_obj)
        # spor_salonu_obj.salonaEkle(a)
        # spor_salonu_obj.salonaEkle(b)
        #yeni_paket.salonaEkle(spor_salonu_obj)

    elif (işlem == "4"):
        spor_salonu_obj.bilgileriGoster()
        
    elif (işlem == "5"):


        isim= input("Ekelemek istediginiz spor aletinin ismini giriniz ")
        tarih= time.time()
        bakim_maliyeti= input("Aletin bakim maliyetini sayi olarak giriniz")
        tamir_maliyeti= input("Aletin tamir maliyetini sayi olarak giriniz")
        try:
            tarih=int(tarih)
            bakim_maliyeti=int(bakim_maliyeti)
            tamir_maliyeti=int(tamir_maliyeti)
            yeni_alet = alet(isim, tarih, bakim_maliyeti, tamir_maliyeti,spor_salonu_obj)
            
        except:

            print("Lutfen tarih,bakim_maliyeti,tamir_maliyetini sayi olarak giris yapiniz")

        
    elif (işlem == "6"):
        
        isim = input("Uye ismini giriniz ")
        soyisim = input("Uye soyismini giriniz ")
        uye_butce = input("Uyenin butcesini giriniz ")

            
        
        try:
            uye_butce=int(uye_butce)
            yeni_abone = abone(isim,soyisim,uye_butce)
            

        except:

            print("Lutfen uye butcesini sayi olarak giris yapiniz")

        
        saglik_raporu = input("Aile Hekiminizden aldiginiz saglik raporunu teslim etmek icin e'ye basiniz ")
        
        if( saglik_raporu == 'e') :
            yeni_abone.saglikRaporuEkle()
        
        veznedar.uyeKaydet(yeni_abone,spor_salonu_obj)  
    
    
    elif (işlem == "7"):
        
        veznedar.aletDurumSorgula(spor_salonu_obj)





    elif (işlem == "8"):
        spor_salonu_obj.butce += veznedar.gunluk_kasa
        veznedar.gunluk_kasa = 0

    elif (işlem == "9"):
        veznedar.gunluk_kasa += spor_salonu_obj.butce 
        spor_salonu_obj.butce = 0

    elif (işlem == "10"):
        print("Günlük Kasa Tutari: ", veznedar.gunluk_kasa)
    
    elif (işlem == "11"):
        print("Spor Salonu Kasa Tutari: ", spor_salonu_obj.butce)
    elif (işlem == "12"):
        sil=veznedar.saglikRaporSorgula(spor_salonu_obj)
        if not sil==None:
            for uye in sil:
                print(uye.isim +"  "+uye.soyisim+"  kaydi siliniyor")
                
                spor_salonu_obj.uyeler.remove(uye)

        


    else:
        print("Geçersiz İşlem...")







