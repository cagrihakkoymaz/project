# from kisi import *
from classes.kisi import kisi

# from abone import *
from classes.kisisel_koc import kisiel_koc
from classes.abone import abone
from classes.veznedar import veznedar
import datetime

from classes.abonelik_paketleri import abonelik_paketleri

standart_paket = abonelik_paketleri("standart",500,5)
baslangic_paket = abonelik_paketleri("baslangic",300,3)
premium_paket = abonelik_paketleri("premium",1000,7)


cagri = abone("Cagri","Hakkoymaz",premium_paket,5,9999999)
veznedar = veznedar()

veznedar.uyeKaydet(cagri)  

cagri.bilgileriGoster()

cagri.saglikRaporuEkle()


veznedar.uyeKaydet(cagri)

print("*--------------")
cagri.bilgileriGoster()






