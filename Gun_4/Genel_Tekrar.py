# # Print fonksiyonu ve özellikleri
# print("Merhaba Bolu")
# yuz_olcumu = "200"
# tevellut = "1990"
# print("Bizim köyün yüz ölçümü " + yuz_olcumu + " tevellutu " + tevellut)
# print("bizim köyün yüz ölçümü {} tevellutu {}".format(yuz_olcumu,tevellut))
# print("Bizim köyün yüz ölçümü {yo} tevellutu {tv}".format(yo=yuz_olcumu, tv = tevellut))
# print("Bizim köyün yüz ölçümü ".join(yuz_olcumu))
#
# ilk_parça = "Bizim köyün yüz ölçümü"
# print(ilk_parça[0])
# for gelecek_sey in ilk_parça:
#     print(gelecek_sey)
#
# # Değişken türleri ve kullanımları
# ilk = "ornek"
# iki = 10
# uc = 10.0
# ornek = True


# input fonksiyonu ve tip dönüşümleri
# ad = input("Adınız")


# Liste nedir? Nerelerde kullanılır?
# bu_bir_listedir = ["bir","kac","tane", "bilinen","degisken"]
# farkli_liste = ["başka", "liste"]
# bu_bir_listedir.append(farkli_liste)
# print(bu_bir_listedir)






# bu_bir_listedir.append({"bu":"sozluktur"}) #olduğu gibi listenin sonuna ekleyecektir.
# for degisken in bu_bir_listedir:
#     if type(degisken) ==dict:
#         print(degisken.get("bu"))
#         continue
#     print(degisken)
#print(bu_bir_listedir[3][0:2])
# print("Listenin ilk hali:{}".format(bu_bir_listedir))
# siralanmis_liste = sorted(bu_bir_listedir, reverse = True) #Degişkene müdahale etmiyor.
# print("Listenin sorted fonksiyonundan sonraki hali:{}\n Sıralanmış hali:{}".format(bu_bir_listedir, siralanmis_liste))
# bu_bir_listedir.sort() #Değişkene müdahale ediyor.
# print("Sort fonksiyonu çalıştıktan sonraki hali:")
# print(bu_bir_listedir)

# #Sözlükler
# ozel_meyveler = ["portakal", 'çilek', 'mandalina']
# meyveler = {
#     'yaz_meyveleri':
#         {'sevdiklerimiz':{'avakado', 'guantanamo elması','çarkıfelek'},
#          'sevmediklerimiz': {'elma', 'armut', 'kiraz'}
#          },
#     'kis_meyveleri':{
#         'ozlediklerimiz': "portakal çilek mandalina",
#         'efsaneler':0
#         }
#         }
#
#
# print(meyveler['yaz_meyveleri'])
# print(meyveler.get('yaz_meyvelerii'))
#
# if meyveler.get("bahar_meyveleri"):
#     print(meyveler.get("bahar_meyveleri"))
# elif meyveler.get("sonbahar_meyveleri"):
#     print(meyveler.get())
#
# else:
#     meyveler.update({'bahar_meyveleri':{}})





#
#
# l_meyveler = [
#     [
#         ['avakado', 'guantanamo elması', 'çarkıfelek'],
#         ['elma', 'armut', 'kirazz']],
#     [[],
#      [[]]
#
#
#      ]
#
#
# ]
#
# print(meyveler)
#
#
#
# liste1 = ['a','b']
# liste2 = ['c','d']
# liste3 = ['e','f']
# liste4=liste1+liste2+liste3
# print(liste4)
#
# yeni_liste = []
# yeni_liste.extend(liste2)
# yeni_liste.extend([*liste1])
# print(liste1)
# print(liste2)
# print(yeni_liste)

# Koşullu ifadeler
# # for ve while döngüsü
#
# sayilar = []
# for say in range(1,10):
#     sayilar.append(say)
# sayilar = [say for say in range(1,10)]
#
#
#
# sayilar2 = [say*say for say in range(1,10) if say % 2 ==0]



# # fonksiyonlar
# def yazdir(kelime):
#     print(kelime)
#     return 10
# degisken = yazdir('Meyve')
# print(degisken)

# def dongu():
#     for i in range(1,10):
#         yield str(i)
#
#
# generator = dongu()
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print('for')
# for x in generator:
#     print(x)





# def args_yazdir(*args):
#     print(args)

# args_yazdir(1,2,3,4,5,6)

# def kwargs_yazdir(bir =2,**kwargs):
#     print(kwargs)
#     print(bir)
#
# kwargs_yazdir(bir=2, iki =2, uc=3)
#
#
# def args_kwargs_yazdir(ilki,ikinci,*args,bir, hasan, **kwargs):
#     print(ilki)
#     print(ikinci)
#     print(args)
#     print(bir)
#     print(kwargs)
#     print(hasan)
#
#
# args_kwargs_yazdir(9,8,7,8,6,bir=1,hasan=2)



# hata kontrol yapısı
# args ve kwargs
# Varsayılan foksiyonlar (len, type, range)

# # Dosya işlemleri
# def dosya_ac(dosya_ismi):
#     dosya = open(dosya_ismi,'r')
#     return dosya

# def dosya_oku(dosya):
#     return dosya.read()
#
# def dosya_yaz(dosya,*args):
#     pass

dosya_oku = open('dosya.txt','r')
dosya_yaz = open('dosya2.txt','w')
icerik = dosya_oku.read()
yaz = dosya_yaz.write('{}'.format(icerik))



dosya_yaz = open('dosya2.txt','w')
print(dosya_yaz.write(dosya_oku.read()))




#
# print("Hava çok güzel",sep='\t\t')
# cümle = "Hava çok güzel"
# for karakter in cümle:
#     if karakter =='\t\t':
#         print('\t\t')
#         continue
#     print(karakter)
#
# #cumle = "\t\t".join(cumle.split(""))
#
# cumle = cumle.replace('','\t\t')
#

