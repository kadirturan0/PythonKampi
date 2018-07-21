test_degiskeni = "Bu bir test değişkenidir"

print(test_degiskeni.upper()) #String değerlerini büyük harf yapar.
print(test_degiskeni.lower()) #String değerlerini küçük harf yapar.
print(test_degiskeni.capitalize()) #String değerinin ilk karakterini büyük harf yapar.
print(test_degiskeni.split()) #String değerindeki boşlukları göstermez.
print(test_degiskeni.rsplit()) #String değerinin sonundaki boşlukları göstermez.
print(test_degiskeni.lstrip()) #String değerinin başındaki boşluğu göstermez.
print(test_degiskeni.strip().capitalize()) #String değerinin boşuklarını silip ilk harf büüyk yapar.

test_degiskeni2 = "\r\n Bu bir test değişkenidir." # Boşluk ve satır atlar.

