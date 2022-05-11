class alet(object) :

    def __init__(self,alet_ismi, son_bakim_tarihi):
        self.son_bakim_tarihi = son_bakim_tarihi
        self.alet_ismi = alet_ismi

    def bilgileriGoster(self):
        print("SAlet bilgileri gosteriliyor...")
        print("Alet ismi: ",self.alet_ismi) 
        print("son bakim tarihi: ",self.son_bakim_tarihi) 

        