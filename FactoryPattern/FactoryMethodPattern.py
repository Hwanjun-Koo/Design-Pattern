class Robot:
    def speak(self):
        pass
    
class Cat(Robot):
    def speak(self):
        print("meow")
        
class Dog(Robot):
    def speak(self):
        print("bark")
        
class Factory():
    def createRobot(self):
        pass
    
class CatFactory(Factory):
    
    def __init__(self):
        self.cat_count = 0 
    
    def createRobot(self):
        self.cat_count += 1
        return Cat()
    
    def catCount(self):
        return self.cat_count
    
class DogFactory(Factory):
    
    def __init__(self):
        self.dog_count = 0
        
    def createRobot(self):
        self.dog_count += 1
        return Dog()
        
    def dogCount(self):
        return self.dog_count
    
cat_factory = CatFactory()
dog_factory = DogFactory()

cat1 = cat_factory.createRobot()
cat2 = cat_factory.createRobot()
print("We have " + str(cat_factory.catCount()) + " cats.")

dog1 = dog_factory.createRobot()
print(dog_factory.dogCount())