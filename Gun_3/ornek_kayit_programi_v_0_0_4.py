# Öğrenci kayit işlemi
# Öğrenci silme
# Öğrencileri görüntüle
# Öğrencileri temizleme

def ogr_kayit():


    print("Öğrenci Kayıt İşlemi")

    ogr_no = input("Öğrenci numarasını giriniz:")
    dosya.txt = open('veritabani.txt', 'w')
    dosya.txt.write("{}".format(ogr_no))
    dosya.txt.close()

    ogr_adi = input("Öğrenci Adını giriniz:")

    ogr_vize = input("Vize notunu giriniz:")

    ogr_final = input("Final Notunu giriniz")

    print("Kayıt işlemi başarılı")

def main():
    dosya = open('veritabani.txt', 'x')
    dosya = open('veritabani.txt', 'r')
    while True:
        secim= input("""
        1- Öğrenci kayit işlemi
        2- Öğrenci silme
        3- Öğrencileri görüntüle
        4- Öğrencileri temizleme

        """)

        if secim == '1':
            ogr_kayit()

main()


ogrenciler = {
            '1': {'vize': 80, "final": 90},
            '2': {'vize': 60, "final": 100}
        }
print(ogrenciler.get("3"))

# with open('ogrencilerim', 'r') as f:
#     okunan_ogrenciler = f.readlines()
#     print(ogrenciler)
#     for satir in okunan_ogrenciler:
#         print(satir)




with open("ogrencilerim",'a+') as f:
    for ogr_no, notlar in ogrenciler.items():
        f.write("{} {} {}\n".format(ogr_no,
                                    notlar.get('vize'),
                                    notlar.get('final')))

alinan_ogrenciler = {}
with open("ogrencilerim", 'r') as f:
    ogrencilerim =f.readlines()
    ogrencilerim = [x.strip() for x in ogrencilerim]
    print(ogrencilerim)
    for ogrenci in ogrencilerim:
        ara_deg = ogrenci.split(" ")
        ogr_no, vize, final = ara_deg[0], ara_deg[1], ara_deg[2]
        #print(ogr_no, vize, final)
        alinan_ogrenciler.update({ogr_no:{'vize': vize, 'final': final}})
print(alinan_ogrenciler)


