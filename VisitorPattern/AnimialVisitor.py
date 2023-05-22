

class AnimalVisitor:
    def catVisit(self, elem):
        pass
    def dogVisit(self, elem):
        pass
    
class SpeakVisitor(AnimalVisitor):
    def catVisit(self, elem):
        print("Meow")
    def dogVisit(self, elem):
        print("Bark")
        
class NameVisitor(AnimalVisitor):
    def catVisit(self, elem):
        print(f"Cat, {elem.name}")
    def dogVisit(self, elem):
        print(f"Dog, {elem.name}")
        
class Animal:
    def __init__(self, name:str):
        self.name = name
    def accept(self, visitor:AnimalVisitor):
        pass
    
class Cat(Animal):
    def accept(self, visitor:AnimalVisitor):
        visitor.catVisit(self)
        
class Dog(Animal):
    def accept(self, visitor: AnimalVisitor):
        visitor.dogVisit(self)
        
jindo = Dog('Jindo')
kitty = Cat('Kitty')

jindo.accept(NameVisitor())
kitty.accept(NameVisitor())