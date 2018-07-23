# Öğrenci kayit işlemi
# Öğrenci silme
# Öğrencileri görüntüle
# Öğrencileri temizleme

ogrenciler = {
    '1': {'vize': 80, "final": 90},
    '2': {'vize': 60, "final": 100}

}

try:
    dosya = open('veritababi.txt', 'a+')
except Exception:
    dosya = open('veritabani.txt', 'x')

for ogr_not, notlar in ogrenciler.items():
    dosya.write("{} numaralı öğrenci vizesi: {} finali {}\n".format(
        ogr_not,
        notlar.get('vize'), notlar.get('final')

    ))