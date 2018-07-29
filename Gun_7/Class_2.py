# print(2+6)
# print(2*6)
# print(type(2))
class sayi:
    def __init__(self,deger):
        self.deger=deger

    def __add__(self, other):
        return self.deger + other.deger


class Iki(sayi):
    pass

class Alti(sayi):
    pass

print(Alti(6).deger + Iki(2).deger)