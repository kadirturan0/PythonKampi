#
#
# def us_alma(deger_1, deger_2):
#     sonuc = deger_1**deger_2
#     print("Sonuç:{}".format(sonuc))
#     return sonuc
#
# try:
#     deger1 = input("Lütfen ilk değeri giriniz")
#     deger2 = input("Lütfen ikinci değeri giriniz")
#     sonucu = us_alma(deger1,deger2)
# except ValueError as e:
#     print(e)
#     print("Hata: Lütfen sayı giriniz")
#
# except Exception as e:
#     print(e)
#     print("Bir hata oluştu:(:")


# if type(deger1) == int and type(deger2) == int:
#     print("Lütfen sayı giriniz.")
#     print(sonucu)
#
# else:
#     print("Lütfen sayı değeri giriniz.")
#
#
# us_alma(deger1,deger2)
#
#
# def topla_cikarma(say1,say2,topla=True):
#     return say1+say2 if topla else say1-say2 #Kodu en kısa hali
#     # if topla:
#     #     return  say1 + say2
#     # return say1-say2
#
# deger1 = input("Lütfen ilk değeri giriniz")
# deger2 = input("Lütfen ikinci değeri giriniz")
# topla_cikarma(deger1,deger2)
#
# def ornek_fonksiyon(*args):
#
#     print("ahmet",sep="#",end="\n\n")
#
# ornek_fonksiyon("ahmet","mehmet")

def yazdirma(*arg):
    yazdirilacaklar = arg[:-2]
    bitirici = arg[-1]
    ayirici = arg[-2]
    print(*yazdirilacaklar,sep=ayirici,end=bitirici)


    #
    # for kelime in yazdirilacaklar:
    #     print(kelime,end='',sep='')
    #     print(ayirici,end='',sep='')
    # print(bitirici)
yazdirma("ahmet", "mehmet", "ayşe", "fatma", '#22', 'bitirdik')



def kw_yazdirma(**kwargs):
    print(*kwargs.get('yazdirilacaklar'), sep=kwargs.get('ayirici'), end=kwargs.get('bitirici'))

# kw_yazdirma(yazdirilacaklar = ["ahmet", "mehmet", "ayşe", "fatma"], ayirici = '#22', bitirici='bitirdik')

def args_kwarg_yazdirma(*args,**kwargs):
    print(args)
    print(kwargs)
args_kwarg_yazdirma("ahmet",ayirici='#',bitirici = 'bitirici')


def yazdirma(**kwargs):
    print(*kwargs.get(yazdir), sep='#', end='$')

yazdirma()