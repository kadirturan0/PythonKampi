ogrenciler = {
            '1': {'vize': 80, "final": 90},
            '2': {'vize': 60, "final": 100}

        }




def ogrenci_ekle():
    tmp_sayac = 0
    while tmp_sayac != 4:
        ogr_no = input("Öğrenci No Giriniz:")
        tmp_sayac += 1
        if tmp_sayac == 4:
            print("Deneme hakkınızı doldurdunuz")

        if len(ogr_no) == 9:
            print("Öğrenci numarası 9 haneli olmalıdır!")

    ogr_vize = input("Vize notunu giriniz:")
    ogr_final = input("Final notunu giriniz:")
    ogrenciler.update({ogr_no: {'vize': ogr_vize,
                                'final': ogr_final}})








def ogrenci_sil():
    silinecek_ogr_no = input("Lütfen silinecek öğrenci no giriniz.")
    if silinecek_ogr_no in ogrenciler.keys():
        ogrenciler.pop(silinecek_ogr_no)
        print("{} numaralı öğrenci silinmiştir.".format(silinecek_ogr_no))

    else:
        print("{} numaralı öğrenci sistemde bulunamadı".format(silinecek_ogr_no))








def ogrenci_gor():
    for ogr_no, ogr_notlari, in ogrenciler.items():
        print("""
        Öğrenci No:{}
        Öğrenci Vize:{}
        Öğrenci Final: {}
        """.format(ogr_no,
                   ogr_notlari.get('vize'),
                   ogr_notlari.get('final'))

              )







def tum_ogrenci_sil():

    ogrenciler.clear()
    print("Öğrenci listesi başarıyla silindi.")






def cikis():
    pass








def main():
    while True:
        # ogrenciler = {
        #     '1': {'vize': 80, "final": 90},
        #     '2': {'vize': 60, "final": 100}
        #
        # }

        secim = input("""
        Öğrenic Kayıt Programına Hoşgeldiniz
        [e] Öğrenci Ekle                                                                                                                          [E]
        [s] Öğrenci Sil
        [g] Öğrencileri Görüntüle
        [d] Tüm Öğrencileri Sil
        [c] Çıkış 
        """)
        if secim == 'e':
            ogrenci_ekle()
        elif secim == 'g':
            ogrenci_gor()
        elif secim == 's':
            ogrenci_sil()
        elif secim == 'd':
            tum_ogrenci_sil()
main()


