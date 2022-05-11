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
alperen_spor_salonu = spor_salonu("Alp",500)

standart_paket = abonelik_paketleri("standart",500,5, alperen_spor_salonu)
baslangic_paket = abonelik_paketleri("baslangic",300,3, alperen_spor_salonu)
premium_paket = abonelik_paketleri("premium",1000,7, alperen_spor_salonu)



alperen_spor_salonu.bilgileriGoster()


cagri = abone("cagri","Hakkoymaz",58)
veznedar = veznedar()

veznedar.uyeKaydet(cagri,alperen_spor_salonu)  
print("*--------------")



cagri.saglikRaporuEkle()


veznedar.uyeKaydet(cagri,alperen_spor_salonu)  


# print("SANİYE",time.time())
# print(time.asctime( time.localtime(time.time()) ))


# dumble=alet(20,5,dumble)



print("*--------------")
cagri.bilgileriGoster()

print("SALONN")
alperen_spor_salonu.bilgileriGoster()

print("/////////////////////---------------------\\\\\\\\\\\\\\\\")
salon_yoneticisi = salon_yoneticisi("Enes", "Dilsiz",50000)
dumble = alet("dumble",time.time() - 150000,500,2000)
dumble.bilgileriGoster()
b = input("bekleme")

veznedar.aletDurumSorgula(alperen_spor_salonu, dumble,salon_yoneticisi)

dumble.bilgileriGoster()

b = input("bekleme")

veznedar.aletDurumSorgula(alperen_spor_salonu, dumble,salon_yoneticisi)

dumble.bilgileriGoster()











