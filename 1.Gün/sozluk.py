sozluk = {
    'one': 'bir',
    'two':[2,10,3,1]

}
print(sozluk.get('two')) #Sözlükten ilgili kelimenin karşılığını gösterir.

sozluk['one'] = 1
print(sozluk)

sozluk.update({'two':2}) #Demeti güncellemenizi sağlar.
sozluk.update({'three':3}) #Demeti güncellemenizi sağlar.
print(sozluk)

sozluk['four'] = 4 #Demete eklemenizi sağlar.
print(sozluk)

del sozluk['one'] #Eleman silmenizi sağlar.
#  del sozluk[2] #Eleman silmenizi sağlar ama önerilen bir metot değildir.

print(sozluk)
sozluk.pop('two') #Eleman silmenizi sağlar.
print(sozluk)

print(sozluk.items()) #Hepsini listeler.
print(sozluk.keys()) #Anahtarları listeler.
print(sozluk.values()) #Değerleri listeler.
