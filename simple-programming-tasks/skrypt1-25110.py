# Napisz program (na dwa sposoby), 
# który sprawdza czy wczytany pojedynczy znak jest cyfrą lub nie.
# Jeśli wczytamy więcej znaków, należy wziąć tylko pierwszy.
# Hint: skorzystaj z funkcji isdigit() i isinstance().

wejscie = input("Podaj liczbę sposob 1:")
if (wejscie[0].isdigit()):
    print("jest cyfra!")
else:
    print("nie jest cyfra")

wejscie = input("Podaj liczbę sposob 2:")
try:
    if (isinstance(int(wejscie[0]),int)):
        print("jest cyfra!")
except:
    print("nie jest cyfra")