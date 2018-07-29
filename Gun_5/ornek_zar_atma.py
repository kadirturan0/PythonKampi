import random

def zar():
    while True:
        puan=0
        tahmin = int(input("Birinci zar tahmini:"))
        tahmin2 = int(input("İkinci zar tahmini:"))
        print("Çıkmak için x yazarak enter tuşuna basınız")

        x = random.randint(0,6)
        y = random.randint(0, 6)
        print(x,y)

        if tahmin ==7:
            print("Çıkış Yaptınız")
            print("Genel Puan:".format(print(puan)))
            break

        elif tahmin == x:
            if tahmin2 ==y:
                puan = puan+1

        else:
            puan=puan-1

        print(puan)






zar()