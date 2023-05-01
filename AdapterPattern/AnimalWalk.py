class Animal:
    def walk(self):
        pass
    
class Cat(Animal):
    def walk(self):
        print("cat walk")
        
class Dog(Animal):
    def walk(self):
        print("dog walk")
        
class Fish:
    def swim(self):
        print("fish swim")
        
class FishAdapter(Animal):
    def __init__(self, fish:Fish): #위임 발생
        self.fish = fish
        
    def walk(self):
        self.fish.swim()
    
def makeWalk(animal: Animal):
    animal.walk()
nemo = Fish()
adapted_nemo = FishAdapter(nemo)
makeWalk(adapted_nemo)
