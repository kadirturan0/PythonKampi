demet = ('a','b','c') #Değiştirilemez
dizi = ['a','b','c'] #Değiştirilebilir
kume = {'a','b','c','a'} #Her eleman en fazla bir kez bulunabilir.

print(demet)
print(dizi)
print(kume)

print(set(dizi))

sehir = 'ankara'
sehir2 = 'istanbul'
print(set(sehir))
sehir2_kume = set(sehir2)

birlesik_kume = sehir2_kume.union(sehir2_kume)
print(birlesik_kume)

dizi_birlesik_kume = list(birlesik_kume)
print(dizi_birlesik_kume)

print("-".join(sehir)) #Karakteri harflere böler ve araya belirlenen karakteri ekler.
print()