import json
from pprint import pprint

class Rehber:

    rehber_bilgileri = {}

    def bilgiler(self,adi,soyadi,numarasi):
        self.adi=adi
        self.soyadi=soyadi
        self.numarasi=numarasi

    def bilgi_yaz(self):


        self.adi = input("Ad: ")
        self.soyadi = input("Soyad: ")
        self.numarasi = input("Numarasi: ")

        with open('rehber_bilgileri.json', "a+") as f:
            json.dumps(Rehber.rehber_bilgileri, f)
            f.write("{}|{}|{}\n".format(self.adi,self.soyadi,self.numarasi))
        return print("İşlem Tamamlandı")



    def bilgi_oku(self):
        with open('rehber_bilgileri.json', 'r') as f:
            bilgiler = json.load(f)
            print(bilgiler)




if __name__ == '__main__':
    while True:
        secim = int(input(print("""
        REHBER UYGULAMASI
        [1] Kişi Ekle
        [2] Kişi Sil
        [3] Kişi Görüntüle
        [4] Tüm Kişileri görüntüle
        [5] Çıkış
        """)))

        if secim==1:
            Rehber().bilgi_yaz()
        if secim==4:
            Rehber().bilgi_oku()