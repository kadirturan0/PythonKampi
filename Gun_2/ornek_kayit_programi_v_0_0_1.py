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








# def menu():
#
#         print("[1] Öğrenci Ekle")
#         print("[2] Öğrenci Sil")
#         print("[3] Öğrencileri Görüntüle")
#         print("[4] Çıkış")
#         secim = int(input("Seçim yapınız: "))
#         if secim == "4" or exit == "Çıkış":
#             exit(0)
#         secim = int(secim)
#
#         vize_final_notlari = {}
#         if secim == 1:
#             while True:
#                 ogrenci_no = input('Öğrenci No')
#                 ogrenci_ismi = input('Öğrenci İsmi:')
#                 vize_notu = int(input('Vize Notu:'))
#                 final_notu = int(input('Final Notu:'))
#                 vize_final_notlari.update({ogrenci_ismi: {
#                      'no':ogrenci_no,
#                      'vize': vize_notu,
#                      'final': final_notu
#                             }})
#                 print("Öğrenci Ekleme işlemi Başarılı")
#                 break
#


while True:

    ogrenciler = {
        '1' : {'vize':80,"final":90},
        '2' : {'vize':60,"final":100}

    }

    secim = input("""
    Öğrenic Kayıt Programına Hoşgeldiniz
    [e] Öğrenci Ekle                                                                                                                          [E]
    [s] Öğrenci Sil
    [g] Öğrencileri Görüntüle
    [d] Tüm Öğrencileri Sil
    [c] Çıkış 
    """)

    if secim == 'e':
        tmp_sayac = 0
        while True:
            ogr_no = input("Öğrenci No Giriniz:")
            tmp_sayac +=1
            if tmp_sayac == 4:
                print("Deneme hakkınızı doldurdunuz")
            break
            if len(ogr_no) == 9:
                print("Öğrenci numarası 9 haneli olmalıdır!")
                continue
        ogr_vize = input("Vize notunu giriniz:")
        ogr_final = input("Final notunu giriniz:")
        ogrenciler.update({ogr_no:{'vize':ogr_vize,
                                   'final':ogr_final}})
    elif secim == 'g':
        # for ogr_numara in ogrenciler:
        #     print("""Öğrenci no:{}
        #     Öğrenci Vize {}
        #     Öğrenci Final {}
        #
        #     """.format(ogrenciler(ogr_numara,
        #                ogrenciler[ogr_numara].get('vize'),
        #                ogrenciler[ogr_numara].get('final'))
        #                ))

        for ogr_no,ogr_notlari, in ogrenciler.items():
            print("""
            Öğrenci No:{}
            Öğrenci Vize:{}
            Öğrenci Final: {}
            """.format(ogr_no,
                       ogr_notlari.get('vize'),
                       ogr_notlari.get('final'))

                  )

    elif secim == 's':
        silinecek_ogr_no = input("Lütfen silinecek öğrenci no giriniz.")
        if silinecek_ogr_no in ogr_notlari.keys():
            ogrenciler.pop(silinecek_ogr_no)
            print("{} numaralı öğrenci silinmiştir.".format(silinecek_ogr_no))

        else:
            print("{} numaralı öğrenci sistemde bulunamadı".format(silinecek_ogr_no))

    elif secim == 'c':
        pass
    elif secim == 'd':
        ogrenciler.clear()
        print("Öğrenci listesi başarıyla silindi.")
    else:
        print("Bilinmeyen bir komut girdiniz!")




