class Ogrenci:
    def __init__(self,isim, soyisim, numara, vize, final):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.vize = vize
        self.final = final

    def goruntule(self):
        print(f"Ögrenci İsmi: {self.isim}\n"
              f"Öğrenci Numarası: {self.numara}\n"
              f"Öğrenci Ortalaması: {self.ortalamasi()}")

    def ortalamasi(self)
        return self.vize * 0.4 + self.final * 0.6

class Sinif:
    ogrenciler = []
    def ogrenci_ekle(self):
        try:
            isim = input("Öğrencinin İsmi")
            soyisim = input("Öğrencinin Soyismi")
            numarasi = input("Numarasi")
            vize = int(input("Öğrenci Vizesi"))
            final = int(input("Öğrenci Finali"))
            dogukan = Ogrenci(isim, soyisim, numarasi, final=final, vize=vize)
            return True
        except Exception as e:
            print(e)
            return False

    def ogrencileri_goruntule(self):
       for ogrenci in self.ogrenciler:
           ogrenci.goruntule

    def ogrenci_sil(self):
        ogrenci_no =input("Öğrenci Numarası")
        self.ogrenciler = list(filter(lambda x:x.numara != ogrenci_no,
                                      self.ogrenciler))

    def sinif_ortalamasi(self):
        from functools import reduce
        reduce(lambda x,y: x.ortalamasi()+y.ortalamasi() , self.ogrenciler/len(self.ogrenciler))
        return ortalama

    def dosyaya_kaydet(self):
        with open('ogrenciler.txt',"+w") as f:
            for ogrenci in self.ogrenciler:
                f.write(ogrenci.

 if __name__ == '__main__':
    python_1b = Sinif
    python_1b.ogrenci_ekle()
    python_1b.ogrencileri_goruntule()
