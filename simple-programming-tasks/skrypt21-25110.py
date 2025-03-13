#Dziedziczenie klas. Klasa Animal ma zawierać atrybuty 
# takie jak name, age, sex oraz metodę sound().
#  Klasy Dog, Cat oraz Fox dziedziczą po klasie 
# Animal oraz nadpisują funkcje sound() odpowiednimi 
# dźwiękami, dodatkowo klasy Dog oraz Cat posiadają atrybut breed.

class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def sound(self):
        return (self.__class__.__name__ + " is barking")
class Fox(Animal):
    def __init__(self,name,age,sex):
         super().__init__(name,age,sex)
class Dog(Animal):
    def __init__(self,name,age,sex,breed):
         super().__init__(name,age,sex)
         self.breed = breed
class Cat(Animal):
    def __init__(self,name,age,sex,breed):
         super().__init__(name,age,sex)
         self.breed = breed

dog1 = Dog("burek","5","male","husky")
print(str(dog1.name)+str(dog1.age)+str(dog1.sex)+str(dog1.breed))