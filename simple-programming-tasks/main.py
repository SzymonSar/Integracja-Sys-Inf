# skrypt 18
# Stworzyć plik funkcje.py, w którym należy zaimplementować funkcję:
#  dodawanie, odejmowanie, dzielenie, mnożenie oraz modulo.
#  W pliku main.py zaimportować plik funkcje.py 
# i wykorzystać zaimportowane funkcje na przykładowych wartościach.

from skrypt18 import funkcje
x = 9
y = 3
print("x = 9, y = 3")

print("dodawanie " + str(funkcje.dodawanie(x,y)))
print("odejmowanie " + str(funkcje.odejmowanie(x,y)))
print("dzielenie " + str(funkcje.dzielenie(x,y)))
print("modulo " + str(funkcje.modulo(x,y)))
