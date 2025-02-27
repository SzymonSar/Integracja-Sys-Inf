#Napisz program (na dwa sposoby), 
# który szuka pierwiastków liczb od 1 do 256
#  (włącznie) podzielnych bez reszty przez 2.
# Hint: skorzystaj z modułu math i z tzw. 'list comprehensions'.
import math

print("sposob1: ")
for i in range(256):
    if math.sqrt(i)%2 == 0:
        print(i)

pierw = [math.sqrt(x)%2 for x in range(256)]
pierw_zera = [i for i, x in enumerate(pierw) if x == 0]
print("sposob2: ",pierw_zera)

