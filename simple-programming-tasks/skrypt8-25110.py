#Napisz program, który generuje losowy ciąg znaków o długości 100,
#  a następnie utwórz słownik którego kluczami będą unikalne znaki
#  występujące w ciągu, a wartościami liczba ich wystąpień w ciągu 
# znakowym. Utwórz listę, której każdy element to krotka (tupla), 
# zawierająca kolejny klucz z ww. słownika i odpowiadającą mu wartość liczbową.

import random
import string

ciag = "".join(random.choice(string.printable) for x in range(1,100))
print("ciag = " +str(ciag))

slownik_temp = {i:ciag.count(i) for i in ciag}

slownik = {}
zbior_liter = set()

for klucz, int in slownik_temp.items():
    if klucz not in zbior_liter:
        slownik[klucz] = int
        zbior_liter.add(int)

print(slownik)