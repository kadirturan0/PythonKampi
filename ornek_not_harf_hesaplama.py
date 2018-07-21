#0-40 DC
#41-60 CC
#61-80 BB
#81-100 AA
#vize = int(input("Vize notunuzu Giriniz:"))     #Programda tip dönüşümü yapmazsak çalışmaz. tip dönüşümü yapmak için int() kullanıyoruz.
#final = int(input("Final notunuzu Giriniz:"))   #Programda tip dönüşümü yapmazsak çalışmaz. tip dönüşümü yapmak için int() kullanıyoruz.

def ortalama_hesapla(gecici_vize,gecici_final):
    print(gecici_vize,type(gecici_vize))
    print(gecici_final,type(gecici_final))
    if type(gecici_vize) == int and type(gecici_final) == int:
        if 0 < gecici_vize < 100 and 0 < gecici_final < 100:

        sonuc = (gecici_vize * 0.4 + gecici_final * 0.6)
        if 0 < sonuc <= 40:
            print("Notunuz DC")

        elif 40<sonuc<=60:
            print("Notunuz CB")

        elif 61<sonuc<=80:
            print("Notunuz BB")

        elif 81<sonuc<=100:
            print("Notunuz AA")

        else:
            print("Tanımsız")
    else:
        print("Lütfen sayı giriniz")

ogr_1_vize = int(input("Vize notunu giriniz:"))
ogr_1_final = int(input("Final notunu giriniz:"))
ortalama_hesapla(ogr_1_vize,ogr_1_final)
