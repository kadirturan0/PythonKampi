
birler = ["sıfır","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

sayi = "123"
sayi = sayi[::-1]

okunus = []
okunus.append(birler[int(sayi[0])])

if len(sayi) >= 2:
    okunus.append(onlar[int(sayi[1])])
if len(sayi) >= 3:
    okunus.append(birler[int(sayi[2])] + "yuz")
if len(sayi) >= 4:
    okunus.append(birler(sayi[3],"bin"))

print(okunus)
print(" ".join(okunus[::-1]))