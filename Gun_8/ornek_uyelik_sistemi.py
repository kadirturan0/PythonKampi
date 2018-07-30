class Uyelik_Sistemi:

    def __init__(self,k_adi,parola,eposta,isim,soyisim):
        self.k_adi = k_adi
        self.parola = parola
        self.eposta = eposta
        self.isim = isim
        self.soyisim = soyisim

    def uye_ekle(self):

        uye_bilgi = open('uye_bilgileri.txt', 'a+')
        veriler = []
        self.k_adi = input("Kullanıcı Adı Giriniz: ")
        self.parola = input("Giriş Parolanızı Giriniz: ")
        self.eposta = input("Eposta Adresinizi Giriniz: ")
        self.isim = input("Adınızı Giriniz: ")
        self.soyisim = input("Soyadınızı Giriniz: ")
        veriler.append()

class Giris_Sistemi:
    def giris(self):

        oku = open('uye_bilgileri.txt', 'r')

        print("""
        ÜYE GİRİŞ EKRANI
        """)
        print("Lütfen Kullanıcı Adınız giriniz: ")


        print("Lütfen Parolanızı giriniz: ")




if __name__ == '__main__':

    secim = int(input(print("""
    ÜYELİK SİSTEMİNE HOŞ GELDİNİZ
    [1] Admin Girişi
    [2] Kayıt Ol
    """)))

    if secim == 1:
        Giris_Sistemi().giris()

    if secim == 2:
        Uyelik_Sistemi().uye_ekle()

