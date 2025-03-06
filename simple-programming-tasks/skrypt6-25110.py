#Napisz program, który tworzy słownik
# o nazwie zawierającej Twój numer albumu.
# Kluczami powinny być liczby od 10 do 20,
# a wartościami pseudolosowe łańcuch znaków o długości 8.
#Hint: skorzystaj z modułów string i random.
import random
import string

slownik25110 = {i: "".join(random.choice(string.printable) for x in range(1,8)) for i in range(10, 20)}

print(slownik25110)