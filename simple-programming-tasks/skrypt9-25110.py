#Stwórz klasy Vehicle i Car z polami nazwa, rok_produkcji i przebieg
#  oraz metodami is_old() i is_long_mileage(). Stwórz po jednym obiekcie
#  dla każdej z klas oraz trzeci obiekt, gdzie klasa Car dziedziczy z klasy Vehicle.
#  Dla każdego z obiektów wywołaj obie metody,
#  co najmniej raz użyj dekoratora @property w każdym z trzech przypadków.

class Vehicle:
    def _init_(self, rok_prod, przebieg):
        self.rok_prod = rok_prod
        self.przebieg = przebieg
    def is_old(self):
        if self.rok_prod < 1970:
            return True
        else:
            return False
    def is_long_mileage(self):
        if self.przebieg > 20000:
            return True
        else:
            return False
        
class Car(Vehicle):
    def __init__(self, rok_prod, przebieg):
        super().__init__(rok_prod, przebieg)


    
    