lass Kullanici:
    def _init_(self, k_adi, parola, eposta, isim, soyisim, veritabani = "ogrenciler.txt"):
        self.k_adi = k_adi
        self.parola = parola
        self.eposta = eposta
        self.isim = isim
        self.soyisim = soyisim
        if not self.varlik_kontrolu(self.k_adi):
            with open(veritabani , "a+") as f:
              f.write("{}|{}|{}|{}|{}\n".format(self.k_adi,
                                              self.parola,
                                              self.eposta,
                                              self.isim,
                                              self.soyisim))
    staticmethod
    def varlik_kontrolu(k_adi, veritabani = "ogrenciler.txt"):
        kullanicilar = []
        with open(veritabani, 'r') as f:
            str_kul = f.readLines()
            kullanicilar.extend([x.split("|")[0] for x in str_kul])
        resp = list(filter(lambda x: x == k_adi, kullanicilar))
        return bool(len(resp))

    def goruntule(self):
        print(f"Kullanıcı adı: \t{self.k_adi}{self.eposta}{self.isim}{self.soyisim}")



class EyesBook:
    kullanicilar = []
    def _init_(self):

     def kayit(self, k_adi, parola, eposta, isim, soyisim):
        self.kullanilar.append(Kullanici(k_adi,parola,eposta=eposta,isim=isim,soyisim=soyisim))

     def giris(self, k_adi,parola):
        # if not Kullanici.varlik_kontrolu(k_adi):
            # pass
            #else:


        while True:

            soru1 = input("Eposta adresi:")
            soru2 = input("Parola:")

            if soru1 == Kullanici and soru2 == parola:
                print("Kullanıcı adı ve parolanız onaylandı."
                      "HOŞGELDİNİZ.")
                break
            else:
                print("Kullanıcı adı veya parolanız yanlış girildi."
                      "TEKRAR DENEYİNİZ.")

    def tumunu_goruntule(self):
        pass

if __name__ == '__main__':
    ornek = Kullanici("Sevim_keskin", "1234", "svmkskn8@hotmail.com", "Sevim", "Keskin")
    resp = Kullanici.varlik_kontrolu("Sevim_keskin")
    ornek.goruntule()
    print(resp)

    eyesbook = EyesBook()
    print("EyesBooka hoşgeldiniz")
    while True:
        secenek = ("Kayit icin 1'e basiniz\n"
                   "Giris icin 2'ye basiniz\n")

        if secenek == "1":
            k_adi = input("kullanici adini girin:")
            parola = input("Parolayı giriniz")
            eposta = input("Epostayı giriniz")
            isim = input("İsimi giriniz")
            soyisim = input("Soyismi giriniz")
            eyesbook.kayit(k_adi,parola,isim,soyisim,eposta)
        elif secenek == "2":
          k_adi = input("kullanici adini girin")
          parola = input("parola giriniz")
          eyesbook.giris(k_adi,parola)
        else:
            break