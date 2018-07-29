ogrenciler = {
            '1': {'vize': 80, "final": 90},
            '2': {'vize': 60, "final": 100}

        }

try:
    dosya = open('ogrenciler.txt','a+')
except Exception:
    dosya = open('ogrenciler.txt', 'x')

for ogr_not,notlar in ogrenciler.items():
    dosya.write("{} numaralı öğrenci vizesi: {} finali {}\n".format(
        ogr_not,
        notlar.get('vize'),notlar.get('final')
        
    ))