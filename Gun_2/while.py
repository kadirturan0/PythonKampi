sayac = 0
while True:
    sayac +=1
    print("Sonsuza dek çalış")
    if sayac == 10:
        break #Döngüyü bitiriyor.


sayac = 0
while True:
    sayac +=1
    if sayac == 100:
        break
    if sayac % 2 ==0:
        continue
    print(sayac)