def yazdir_soz():
    print("Merhaba Dünya")
    print("Merhaba Mars")

def iki_defa_yazdir():
    yazdir_soz()
    yazdir_soz()

#iki_defa_yazdir()

def dondur_soz():
    return "Merhaba Dünya"

def yazdir(soz):
    print(soz)

yazdir(dondur_soz())

def iki_yazdir(soz):
    print(soz)
    print(soz)
#soz = dondur_soz()
#iki_yazdir(soz)


def hata_dondur():
    raise Exception("Hata")
try:
    degisken=hata_dondur()
    print(degisken)
except:
    print('diğer hata')

def yeni(arg1=10):
    print(arg1)

yeni(30)