class Animal:
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")
        
class AnimalGroup(Animal):
    def __init__(self):
        self.animals = []
    
    def add(self, animal:Animal):
        self.animals.append(animal)
    
    def speak(self):
        print("group speaking")
        for animal in self.animals:
            animal.speak()
            
cat_group = AnimalGroup()
cat_group.add(Cat())
cat_group.add(Cat())
cat_group.add(Cat())

dog_group = AnimalGroup()
dog_group.add(Dog())
dog_group.add(Dog())

zoo = AnimalGroup()
zoo.add(cat_group)
zoo.add(dog_group)

zoo.speak()