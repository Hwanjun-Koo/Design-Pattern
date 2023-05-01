class Animal:
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        print("Meow")
        
class Lion(Animal):
    def speak(self):
        print("Roar")
        
def makeSpeak(animal:Animal):
    animal.speak()
    
def createAnimal(input_str:str) -> Animal:
    if input_str == "cat":
        return Cat()
    elif input_str == "lion":
        return Lion()
    
input_str = input('Create an animal: ')
animal = createAnimal(input_str)
makeSpeak(animal)
