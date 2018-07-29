class Ogrenci(object):
    def __init__(self,isim,soyisim,numara,anne_adi,baba_adi):
        self.isim= isim
        self.soyisim = soyisim
        self.numara = numara
        self.__anne_adi = anne_adi
        self.__baba_adi = baba_adi

    def ogrenci_goruntule(self):
        print("N:{} İ:{} S:{}".format(
            self.numara,self.isim,self.soyisim
        ))

sezer = Ogrenci('Sezer', 'Bozkır', 120101003,'Gönül','Can')
kadir = Ogrenci('Kadir', 'Turan', 3012324, 'Hüsne', 'Mehmet Ali')

sezer.ogrenci_goruntule()

