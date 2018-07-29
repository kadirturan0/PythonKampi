import math

def hesapla():
    y = int(input("Dairenin yarıcapını giriniz:"))
    cevre = (2*(math.pi)*y)
    print(cevre)
    alan = (math.pi*pow(y,2))
    print(alan)

hesapla()