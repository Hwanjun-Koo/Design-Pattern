import random
class Actor:
    def __init__(self, x, y, vital, agi, str, name):
        self.x = x
        self.y = y
        self.vital = vital
        self.agi = agi
        self.str = str
        self.name = name
    
    def status(self):
        print(f"{self.name} appeared on ({self.x}, {self.y})")
        print(f"Vital: {self.vital} Agility: {self.agi} Strength: {self.str}\n")
    
class CharBuilder:
    def __init__(self):
        self.x = None
        self.y = None
        self.vital = None
        self.agi = None
        self.str = None
        self.name = None
    
    def setName(self, name):
        self.name = name
        return self
        
    def setX(self, x):
        self.x = max(min(x, 100), 0)
        return self
    
    def setY(self, y):
        self.y = max(min(y, 100), 0)
        return self
    
    def setVital(self, vital):
        self.vital = vital
        return self

    def setAgi(self, agi):
        self.agi = agi
        return self
    
    def setStr(self, str):
        self.str = str
        return self
       
    def Build(self):
        character = Actor(self.x, self.y, self.vital, self.agi, self.str, self.name)
        return character

class HeroBuilder(CharBuilder):
    def __init__(self):
        super().__init__()
        self.name = "Hero"
         
    def Build(self):
        character = Actor(self.x, self.y, self.vital, self.agi, self.str, self.name)
        return character

class MonsterBuilder(CharBuilder):
    def __init__(self):
        super().__init__
        self.name = "Monster"
        
hero = (HeroBuilder().setX(101).setY(-1)
        .setVital(100).setAgi(10).setStr(50).Build())
hero.status()

x = random.randint(0, 100)
y = random.randint(0, 100)
v = random.randint(50, 100)
a = random.randint(50, 100)
s = random.randint(50, 100)

monster = (MonsterBuilder().setX(x).setY(y)
           .setVital(v).setAgi(a).setStr(s).Build())
monster.status()
        
    
        