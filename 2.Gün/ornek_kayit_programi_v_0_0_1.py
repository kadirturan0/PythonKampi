#Kullanıcıya ne yapılması gerektiğini sor
    # 1) Öğrenci Ekle
    # 2) Öğrenci Sil
    # 3) Öğrencileri Görüntüle
    # 4) Çıkış

    #Öğrenci eklemek isteniyorsa
    #Öğrenci ismi, vize, final bilgilerini al
    #Sözlüğe ekle
    #Tekrar ana menüye döndür.

    #Öğrenci silmek isteniyorsa
    #Öğrencinin varlığını kontrol et
    #Varsa sil ve "Başarılı" yazdır, yoksa öğrenci bulunamadı
    #Ana menüye döndür

    #Öğrencileri görüntülemek isteniyorsa
    #Öğrenci listesini ekrana yazdır.








def menu():
    try:
        print("[1] Öğrenci Ekle")
        print("[2] Öğrenci Sil")
        print("[3] Öğrencileri Görüntüle")
        print("[4] Çıkış")
        secim = input("Seçim yapınız: ")
        if secim == "4" or exit == "Çıkış":
            exit(0)
        secim = int(secim)

        vize_final_notlari = {}
        if secim == 1:
            while True:
                ogrenci_ismi = input('Öğrenci İsmi:')
                vize_notu = int(input('Vize Notu:'))
                final_notu = int(input('Final Notu:'))

                ortalama = (vize_notu * 0.4 + final_notu * 0.6)
                print(ortalama)

                vize_final_notlari.update({ogrenci_ismi: {
                     'vize': vize_notu,
                     'final': final_notu
                            }})



                print("Öğrenci Ekleme işlemi Başarılı")

        menu()

