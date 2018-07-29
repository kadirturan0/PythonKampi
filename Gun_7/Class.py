class Canli:
    def __init__(self, enerji):
        self.enerji = enerji
    def iletisim(self):
        pass

class Hayvan(Canli):
    def __init__(self,enerji,tur):
        self.enerji=enerji
        self.tur = tur
        super(Hayvan, self).__init__(enerji)

    def yemek_yer(self):
        return 'Besin tüketiliyor'

class Kopek(Hayvan):

    def __init__(self,enerji, isim):
        super(Kopek).__init__(enerji,'memeli')
        self.isim = isim

    def iletisim(self):
        print('Auuu, hav, hav')


canli = Canli(100)
#print(canli.enerji)
hayvan = Hayvan(90,'surungen')
#print(hayvan.enerji)
fiko = Kopek(200,'fiko')
#print(fiko.__dict__.get('isim'))
#print(fiko.isim)

print(hayvan.yemek_yer())
print(fiko.yemek_yer())