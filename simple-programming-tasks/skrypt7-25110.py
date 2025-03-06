#Stwórz folder utils, a w nim plik 'obliczenia.py',
# w którym należy zaimplementować cztery
# wybrane funkcje matematyczne z modułu math.
# Następnie należy utworzyć plik skrypt7-nr_albumu.py
# i zaimportować w nim ww. funkcje do obliczeń
# na przykładowych wartościach.
from utils import obliczenia

a = 10
b = 5

print("a = "+str(a)+"  b = "+str(b))
print("pierwiastek z liczby a: "+ str(obliczenia.pierwiastek(a)))
print("silnia z liczby a: "+ str(obliczenia.silnia(a)))
print("logarytm z liczb a i b: "+str(obliczenia.logarytm(a,b)))
print("potega z liczb a i b: "+str(obliczenia.potega(a,b)))