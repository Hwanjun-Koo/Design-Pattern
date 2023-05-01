from abc import*
import copy

class Dog:
    def __init__(self):
        self.color = None
        self.name = None
        self.size = None
    
    def clone(self):
        return copy.deepcopy(self)
    
class BigDog(Dog):
    def __init__(self):
        super().__init__()
        self.size = 'big'
        
class SmallDog(Dog):
    def __init__(self):
        super().__init__()
        self.size = 'small'
        
big_dog = BigDog()
big_dog.color = 'black'
poppy = big_dog.clone()
poppy.name = 'poppy'

print(poppy.name)