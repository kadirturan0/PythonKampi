class Zaman:

    def __init__(self, tarih):
        self.gun, self.ay, self.yil = map(int, tarih.split('/'))



    def __str__(self):

        return "{gun} / {ay} / {yil} ".format(**self.__dict__)

    def __sub__(self, other):
        return self.yil-other.yil


    def kalan_zaman(self,other):
        pass

if __name__ == '__main__':
    bugun_tarihi = Zaman("28/07/2018")
    dogum_gunum = Zaman("16/12/1993")
    yasi = bugun_tarihi-dogum_gunum
    print("Yaş: ".format(yasi))

