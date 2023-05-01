class Animal:
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        print('A cat', end = ' ')
        
class Dog(Animal):
    def speak(self):
        print('A dog', end = ' ')
        
class Vehicle:
    def __init__(self, animal:Animal):
        self.animal = animal
        
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        self.animal.speak()
        print('drives a car')

class Boat(Vehicle):
    def start(self):
        self.animal.speak()
        print('sails a boat')
        
class Airplane(Vehicle):
    def start(self):
        self.animal.speak()
        print('on a airplane')
        
cat = Cat()
boat = Boat(cat)
boat.start()