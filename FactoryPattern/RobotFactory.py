class Robot:
    def speak(self):
        pass

class Cat(Robot):
    def speak(self):
        print("meow")

class Dog(Robot):
    def speak(self):
        print("bark")
        
def factoryFunc(animal):
    if animal == "cat":
        return Cat()
    elif animal == "dog":
        return Dog()
    
cat = factoryFunc("cat")
dog = factoryFunc("dog")

cat.speak()
dog.speak()
