#Stwórz klasy Vehicle i Car z polami nazwa, rok_produkcji i przebieg
#  oraz metodami is_old() i is_long_mileage(). Stwórz po jednym obiekcie
#  dla każdej z klas oraz trzeci obiekt, gdzie klasa Car dziedziczy z klasy Vehicle.
#  Dla każdego z obiektów wywołaj obie metody,
#  co najmniej raz użyj dekoratora @property w każdym z trzech przypadków.

class Vehicle:
    def __init__(self, rok_prod, przebieg):
        self.rok_prod = rok_prod
        self.przebieg = przebieg
    @property
    def is_old(self):
        if self.rok_prod < 1970:
            return True
        else:
            return False
    @property
    def is_long_mileage(self):
        if self.przebieg > 20000:
            return True
        else:
            return False
        
class Car(Vehicle):
    def __init__(self, rok_prod, przebieg):
        super().__init__(rok_prod, przebieg)

pojazd1 = Vehicle(1990,100000)
auto1 = Car(1990,100000)
auto2_dziedzicz = Car(2010,10000)
print("czy pojazd1 ma długi przebieg? ")
print("Tak") if pojazd1.is_long_mileage else print("Nie")
print("czy pojazd1 jest stary? ")
print("Tak") if pojazd1.is_old else print("Nie")
print("czy auto1 ma długi przebieg? ")
print("Tak") if auto1.is_long_mileage else print("Nie")
print("czy auto1 jest stary? ")
print("Tak") if auto1.is_old else print("Nie")
print("czy auto2 ma długi przebieg? ")
print("Tak") if auto2_dziedzicz.is_long_mileage else print("Nie")
print("czy auto2 jest stary? ")
print("Tak") if auto2_dziedzicz.is_old else print("Nie")
