class Animal:
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        print("meow", end = '')
        
class Dog(Animal):
    def speak(self):
        print("bark", end = '')
        
def makeSpeak(animal:Animal):
    animal.speak()
    print(" ")
    
class Deco(Animal):
    def __init__(self, animal:Animal):
        self.animal = animal
        
    def speak(self):
        self.animal.speak()
        
class Smile(Deco):
    def speak(self):
        self.animal.speak()
        print("(smile)", end = '')
    
kitty = Cat()
makeSpeak(kitty)
kitty_smile = Smile(kitty)
makeSpeak(kitty_smile)