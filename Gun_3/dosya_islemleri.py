dosya = open('dosya.txt.txt')
#print(dosya.txt.read()) #Dosyayı okuma aişlevi görür.
#print(dosya.txt.read()) #Dosya bir kez okunabiliyor. Tekrar okunması için farklı bir değişkene atanması gerekiyor.
#icerik=dosya.txt.read()
#print(icerik)

satirlar = dosya.readline() #Dosyanın sadece ilk satırını okur.
satirlar2 = dosya.readlines() #Dosyadaki her satırı böler.

print(satirlar2)
dosya.close()

# r -> read
# w -> write
# a -> append
# x -> create
dosya = open('dosyam.txt', 'a')


#icerik = dosya.txt.readline()
try:
    dosya = open('dosyam.txt', 'w')
    icerik = dosya.readline()
    # temizlenmis_icerik = []
    # for satir in icerik:
    #     temizlenmis_icerik.append(satir)
    # print(temizlenmis_icerik)
    icerik = [satir.strip() for satir in icerik]
    dosya.close()
except Exception:
    print("Dosya yoktur.")