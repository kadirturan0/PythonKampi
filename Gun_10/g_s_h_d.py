class Sinif:
    ornek = 'degeri'
    def __init__(self):
        self.ornek = 'degeri'

print(Sinif.__dict__)
guncel = setattr(Sinif,'ornek','degeri')
print(guncel,Sinif.ornek)
resp = getattr(Sinif,'ornek')
print(resp)
resp_2 = hasattr(Sinif,'baska')
print(resp_2)
delattr(Sinif,'ornek')