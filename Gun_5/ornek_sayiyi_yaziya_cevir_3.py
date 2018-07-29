dizi = [
    [None,"bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"],
    [None,"on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]]

sayi = "38"
sayi = sayi[::-1]
okunus = []
for i,s in enumerate(sayi):
    print(i,s)
    okunus.append(dizi[i][int(s)])

print(" ".join(reversed(okunus)))
print(okunus)