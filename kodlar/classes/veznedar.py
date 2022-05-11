from classes.kisi import kisi
from classes.abone import abone
from classes.abonelik_paketleri import abonelik_paketleri
import time




class veznedar(kisi):

    def __init__(self):
         pass

    def uyeKaydet(self,abone):
        if(len(abone.saglik_raporlari) != 0):
            abone.status = True
            abone.abonelik_baslangic_tarihi = time.time()
        else:
            abone.status = False
    

    
