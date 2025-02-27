#Napisz program, który szuka określonego ciągu znaków
#  w łańcuchu znakowym i zwraca indeksy wszystkich 
# wystąpień ciągu lub -1, gdy nie ma takiego ciągu.
# Hint: skorzystaj z funkcji split().

#przykladowy input = hi hi hi hello hi hi hello hi hello hi hello
ciag = "hello"
wejscie = input("Podaj ciag znakow i sprawdze gdzie zawiera wszystkie \""+ciag+"\"  ")
podzielone = wejscie.split(sep=ciag, maxsplit=-1)
#zmienna pamietajaca na ktorym miejscu jestem w oryginalnym ciagu znakow przed splitem
miejsce = 0
for i in range(0, len(podzielone)):
    miejsce += len(podzielone[i])
    print("ciag ",i+1," w miejscu ",miejsce)
    miejsce += len(ciag)