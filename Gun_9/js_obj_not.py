#JSON Anlatılacaktır.

import json
from pprint import pprint
kullanıcilar = {
    "excelibur_13":{
        "isim":"Sezer",
        "soyisim":"Bozkir",
        "eposta": "admin@sezerbozkir.com",
        "parola": "123"
    },
    "excelibur_14": {
        "isim": "Elif",
        "soyisim": "türk",
        "eposta": "elif@turk.com",
        "parola": "1234"
    }
}

with open('kullanicilar.json',"w") as f:
    json.dump(kullanıcilar,f)


with open("kullanicilar.json","r") as f:
    cek_kul = json.load(f)
    print(cek_kul)
    print(cek_kul['excelibur_13'])