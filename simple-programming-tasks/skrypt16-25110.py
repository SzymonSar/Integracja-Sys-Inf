#Napisz prostą funkcję o nazwie potega(), przyjmującą jeden argument, podnoszącą podaną liczbę do trzeciej potęgi.

def potega(x):
    return x*x*x
liczba = input("podaj liczbe: ")
print(potega(int(liczba)))