import random
import time
class Memento:
    
    def __init__(self, money):
        self.money = money
        self.fruits = []
        
    def getMoney(self):
        return self.money
    
    def addFruit(self, fruit):
        self.fruits.append(fruit)
        
    def getFruits(self):
        return self.fruits
    
class Gamer:
    
    def __init__(self, money):
        self.money = money
        self.fruits = []
        self.fruitsName = ["Apple", "Grapes", "Banana", "Orange"]
        
    def getMoney(self):
        return self.money
    
    def getFruit(self):
        fruitNum = len(self.fruitsName)
        fruitName = self.fruitsName[random.randint(0, fruitNum - 1)]
        return "Yummy " + fruitName
    
    def bet(self):
        
        dice = random.randint(1, 6)
        
        if dice % 2 == 1:
            self.money -= 100
            print("Lost money")
            
        elif dice % 2 == 0 and dice != 6:
            self.money += 200
            print("Gain money")
            
        elif dice == 6:
            f = self.getFruit()
            print("You got " + f)
            self.fruits.append(f)
            
    def createMemento(self):
        m = Memento(self.money)
        
        for f in self.fruits:
            m.addFruit(f)
            
        return m
    
    def restoreMemento(self, memento):
        self.money = memento.money
        self.fruits = memento.fruits
        
    def printState(self):
        print("[Money: " + str(self.money) + ", Fruits: ", end = '')
        
        for f in self.fruits:
            print(", " + f, end = '')
            
        print("]")
        
def gameRun():
    print("Game Start")
    gamer = Gamer(100)
    memento = gamer.createMemento()
    
    for i in range(10):
        print("===Game turn===, " + str(i + 1))
        gamer.printState()
        
        gamer.bet()
        
        print("Money: " + str(gamer.getMoney()))
        
        if gamer.getMoney() > memento.getMoney():
            print("Saving..")
            memento = gamer.createMemento()
            
        elif gamer.getMoney() < memento.getMoney() / 2:
            print("Loading...")
            gamer.restoreMemento(memento)
            
        time.sleep(0.5)
        print()
        
gameRun()