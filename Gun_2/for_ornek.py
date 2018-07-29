vize_final_notlari = {}

for i in range(2):

    ogrenci_ismi = input('Öğrenci İsmi:')
    vize_notu = int(input('Vize Notu:'))
    final_notu = int(input('Final Notu:'))

    ortalama = (vize_notu * 0.4 + final_notu * 0.6)
    print(ortalama)

    vize_final_notlari.update({ogrenci_ismi:{
        'vize':vize_notu,
        'final':final_notu
    }})



    genel=0
    genel=genel+ortalama

print('Genel Ortalama:{}:'.format(genel/3))

ornek = [10,2,5,1,5,7,9]

for sira, veri in enumerate(ornek):
    print(ornek)

for say in range(1,10,2): #Birden başla ona kadar ikişer ikişer arttır.
    print(say)