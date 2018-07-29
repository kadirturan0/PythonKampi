import random



from random import randint

def tahmin_sonucu(tahmin):
    gelen_zar = randint(1,6)
    print(f"Kandırmıyorum{gelen_zar}")
    return True if randint(1,6) == tahmin else False

def main():
    puan = 0
    print("ZAR OYUNU")
    while True:
        tahmini= int(input("Lütfen tahmininizi giriniz:"))
        if tahmini==0:
            print("Oyundan Çıkıyor")
            break
        if 0<tahmini<7:
            sonuc = tahmin_sonucu(tahmini)
            if sonuc:
                puan +=1
                print("Doğru Tahmin")
            else:
                puan=-1
                print("Yanlış Tahmin")
        else:
            print("Lütfen 1 ve 6 arasında sayi giriniz")
            continue

    else:
        print()






main()