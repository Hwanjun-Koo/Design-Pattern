import time
import random
class Observer:
    def update(self, generator):
        pass
    
class NumberGenerator:
    
    def __init__(self):
        self.observers = []
        
    def addObserver(self, observer):
        self.observers.append(observer)
        
    def deleteObserver(self, observer):
        self.observers.remove(observer)
        
    def notifyObserver(self):
        for obs in self.observers:
            obs.update(self)
            
    def getNumber(self):
        pass
    
    def execute(self):
        pass

class RandomNumberGenerator(NumberGenerator):
    
    def __init__(self):
        super().__init__()
        self.number = 0
        
    def getNumber(self):
        return self.number
    
    def execute(self):
        for i in range(20):
            self.number = random.randint(1, 50)
            self.notifyObserver()
            
class DigitObserver(Observer):
    def update(self, generator):
        print("Digit observer: ", generator.getNumber())
        time.sleep(1)
            
class GraphObserver(Observer):
    def update(self, generator):
            print("Graph observer: ", end = '')
            count = generator.getNumber()
            
            for i in range(count):
                print("*", end = '')
            print()
            
            time.sleep(1)
            
generator = RandomNumberGenerator()
observer1 = DigitObserver()
observer2 = GraphObserver()

generator.addObserver(observer1)
generator.addObserver(observer2)
generator.execute()

            