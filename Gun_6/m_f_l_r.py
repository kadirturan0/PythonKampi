# def carpma(say,say2):
#     return say *say2
#
#
#
# a = lambda say,say2:say*say2   #Yukarıdaki kod ile aynı işlevi görür.
# print(a(10,15))
#
# b = lambda deger:deger #Fonksiyon kullanmak yerine lambda kullanmak bazen daha cazip gelebilir.
# print(b("Örnek"))
#
# def sayi_dondur():
#     for say in range(1,10):
#         yield say
#
# siradaki = sayi_dondur()
# print(siradaki.__next__()) #next fonksiyonu her defasında sonraki değeri getiriyor.
# print(siradaki.__next__())
# print(siradaki.__next__())
#
bir_dizi_var = [5,10,2,18,21,55]
#
# yeni_deger = map(b, bir_dizi_var)
# print(list(yeni_deger))
# print(list(yeni_deger))
#
# string_deger = []
# for deger in bir_dizi_var:
#     string_deger.append(str(deger))
#
# print(bir_dizi_var,string_deger,sep="\n")
#
# yeni_deger = map(lambda deger: str(deger), bir_dizi_var)
# print(list(yeni_deger))


# sonuc = filter(lambda say : say %2 ==0 , bir_dizi_var )
# print(list(sonuc))

from functools import  reduce
print(bir_dizi_var)
toplam=0
for deg in bir_dizi_var:
    toplam += deg
print(toplam)

resp = reduce(lambda x,y : x+y,bir_dizi_var) # Bir üstteki for döngüsü ile aynı işlevi görür.

print(resp)