liste = [1, 2, 3, 4, 5, 7]
print(liste)

liste.append("armut") #Listenin sonuna eleman ekler.

liste.insert(0, "elma") #Listenin başına eleman ekler.

print(liste[2]) #Listenin 3.elemanını gösterir. Listelerde elemanlar sıfırdan başlar.

liste.pop() #Listeden son elemanı almanızı sağlar.

cikarilan =liste.pop()

print(cikarilan)
print(liste)
cikarilan = liste.pop(2) #Üçüncü elemanı çıkarır.

#cikti = liste.remove("3")
#print(liste)

cikarilan2 = liste.remove(liste[2]) #Listeden eleman çıkarmanın başka bir yolu
print(cikarilan)


liste2 = [5,4,3,2,1]
liste.append(liste2) #Listeleri birleştirir.

liste.extend(liste2)
print(liste)

liste3 = sorted(liste2)
print(liste2)
print(liste3)

liste4 = [2,4,5,7,9,6]
liste4.sort(reverse=True) #Listedeki elemanları büyükten küçüğe doğru sıralar.
print(liste4)

liste4.reverse()
print(liste4)

print(liste4.count(1))
print(len(liste4))