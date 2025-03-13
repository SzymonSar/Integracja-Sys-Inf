#Używając pętli wyświetl liczby w przedziale od 1 do 100 podzielne przez 3 i 4 oraz podaj ich liczbę.

liczba = 0
for x in range(100):
    if (x+1)%3==0 and (x+1)%4==0:
            print(x+1)
            liczba += 1
print("liczba: "+str(liczba))