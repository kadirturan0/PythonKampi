class Ogrenci:
    def ortalama(self):
        pass

    def __init__(self, numara, isim, soyisim, vize, final):
        self.numara = numara
        self.isim = isim
        self.soyisim = soyisim
        self.vize = vize
        self.final = final


class Sinif:
    def ogrenci_ekle(self):

        ogrenciler = []
        self.numara  = input("Öğrenci No: ")
        self.isim    = input("Öğrenci Adı: ")
        self.soyisim = input("Öğrenci Soyadi: ")
        self.vize    = input("Vize Notu: ")
        self.soyisim   = input("Final Notu: ")

        ogrenciler.append(Ogrenci())

    def ogrenci_sil(self):
        pass

    def ogrenci_goruntule(self):
        print("N:{} İ:{} S:{}".format(
            self.numara,self.isim,self.soyisim
        ))

    def sinif_ortalamasi(self):
        pass



def main():



    while True:
        secim= int (input(print("""
        [1] Öğrenci Ekle
        [2] Öğrenci Sil
        [3] Öğrencileri Görüntüle
        [4] Genel Ortalama
        [5] Tüm Öğrencileri Görüntüle
        [6] Çıkış
        """)))

        if secim == 1:
            Ogrenci.ogrenci_ekle()
        elif secim == 2:
            Ogrenci.ogrenci_sil()



main()