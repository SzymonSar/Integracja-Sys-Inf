#Należy wykorzystać plik wordlist_10000.txt
# i stworzyć funkcję wyszukującą najdłuższy wyraz w tym pliku
#  oraz drugą funkcję, która wyszuka wyrazy o długości 10.

def szukanie_najdluzszy():
    with open("wordlist_10000.txt", 'r') as plik:
        naj_dlug = 0
        for numer_linii, linia in enumerate(plik, start=1):
            if (len(linia)>naj_dlug):
                naj_dlug=len(linia)
        return naj_dlug

def szukanie_dlug(dlug):
    with open("wordlist_10000.txt", 'r') as plik:
        liczba = 0
        for numer_linii, linia in enumerate(plik, start=1):
            if (len(linia)==dlug):
                liczba+=1
        return liczba

print(str(szukanie_najdluzszy()))
print(str(szukanie_dlug(10)))