ornek = "Bugün hava çok güzel"
ornek2 = "Bugün Perşembe"
ozel_sayim = 13
print(ornek.capitalize()) #İlk harfi büyük yapar.
print(ornek.upper()) #Tümünü büyük yapar.
print("Bugü hava çok güzel" + ornek)
print("Bugün hava çok güzel: {}".format(ornek))
print("Bugün hava çok güzel:",ornek,ornek2, ozel_sayim)
print(ozel_sayim is None)
print(ozel_sayim == None)

Meyveler = ["elma", "armut", "havuç"]
print(Meyveler.append("kiraz")) #Listeye ekleme yapmanızı sağlar.
print(Meyveler)

Meyveler.insert(0,"avakado") #Başa eklememizi sağlar.
print(Meyveler)

ozel_sayilar = [10,2,5,21,16]
ozel_sayilar.reverse() #Tersten sıralar.
print(ozel_sayilar)
ozel_sayilar.sort()
print(ozel_sayilar) #Büyükten küçüğe doğru sıralar.

#Sozluk
varsayilan_not = { "vize":0, "final":0}

ogrenciler={
    'Sezer Bozkır' : {'vize':80,
                      'final':90
                      },
    'Kadir turan'  : {'vize':60,
                      'final':90
                      }
}

if ogrenciler.get('Enes Şahin') == None:
    ogrenciler.update({'Enes Şahin': varsayilan_not,

                       'Mehmet Turan': varsayilan_not})

print(ogrenciler.get('Mehmet Turan',varsayilan_not))
print(ogrenciler)
print(ogrenciler.items())


for ogrenci, notu in ogrenciler.items():
    ogrenciler[ogrenci]['vize'] = 0



