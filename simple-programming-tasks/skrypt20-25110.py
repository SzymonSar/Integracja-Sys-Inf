#Prosta gra, program generuje losową liczbę od 1 do 100,
#  użytkownik ma odgadnąć liczbę, jeżeli nie trafi ma zostać 
# wyświetlona podpowiedź czy za duża czy za mała liczba.
import random
liczba = random.randint(1,100)
zgadniecie = False
while(zgadniecie == False):
    strzal = int(input("zgadnij liczbe strzelajac: "))
    if(liczba<strzal):
        print("Strzał za duzy")
    if(liczba>strzal):
        print("strzal za maly")
    if(liczba==strzal):
        zgadniecie = True
        print("Zgadles")