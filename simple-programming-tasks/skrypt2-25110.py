# Napisz program, który sprawdza czy 
# wczytany łańcuch znakowy jest liczbą lub nie.
# Muszą być wczytane co najmniej dwa znaki.
# Hint: skorzystaj z funkcji all().

wejscie = input("Podaj dane 2 symbole lub wiecej:")
if len(wejscie)>=2:
    try:
        if (isinstance(int(wejscie[0]),int)):
            print("jest liczba!")
    except:
        print("nie jest liczba")
else:
    print("za malo symboli")