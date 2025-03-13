#Stwórz klasę o nazwie Dog, która będzie posiadała zmienne takie jak:
#  name, age, coat_color. Dodatkowo klasa posiada funkcje sound(),
#  po wywołaniu której wypisywany jest tekst: {name} is barking!
#  Stworzyć 3 obiekty klasy Dog.

class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color=coat_color
    def sound(self):
        return (self.__class__.__name__ + " is barking")

dog1 = Dog("burek","5","biały")
dog2 = Dog("reksio","6","szary")
dog3 = Dog("keksik","7","czarny")
print(dog1.name)
print(dog1.sound())
