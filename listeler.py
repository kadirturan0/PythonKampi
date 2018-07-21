liste = [4, 2, 6, 6, "Elma", 5]
print(liste)

liste.append("armut") #Listenin sonuna eleman ekler.

liste.insert(0, "yeni") #Listenin başına eleman ekler.
print(liste[2]) #Listenin ikinci 3.elemanını gösterir. Listelerde elemanlar sıfırdan başlar.
liste.pop() #Listeden son elemanı almanızı sağlar.

cikarilan =liste.pop()

print(cikarilan)
print(liste)
cikarilan = liste.pop(2) #Üçüncü elemanı çıkarır.

cikti = liste.remove("Elma")
print(liste)