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

print('Genel Ortalama{}:'.format(genel/3))




