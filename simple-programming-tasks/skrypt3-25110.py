# Napisz program, który szuka określonego 
# ciągu znaków w łańcuchu znakowym i 
# zwraca indeks pierwszego wystąpienia ciągu lub -1,
# gdy nie ma takiego ciągu.
# Hint: skorzystaj z funkcji find().

#przykladowy input = hi hello hi
ciag = "hello"
wejscie = input("Podaj ciag znakow i sprawdze gdzie zawiera \""+ciag+"\"  ")
print ("ciag znajduje się w pozycji ",wejscie.find(ciag))

