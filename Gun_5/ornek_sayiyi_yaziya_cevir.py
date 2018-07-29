def sayi_yazdir(say):
    birler = ["sıfır","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    onlar = ["on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

    basamak_degeri = len(say)
    if basamak_degeri ==1:
        print(birler[int(say)])
    elif basamak_degeri==2:
        if say[1] !=0:
            print(onlar[int(say[0])],birler[int(say[1])])
        else:
            print(onlar[int(say[0])],birler[int(say[1])])
    elif basamak_degeri ==3:
        if int(say[0]) !=1:
            print(birler[int(say[0])], "yuz", onlar[int(say[0])],birler[int(say[1])])
        else:
            print("yuz", onlar[int(say[1])], birler(say)[2])


say = input("Sayi Giriniz:")
sayi_yazdir()