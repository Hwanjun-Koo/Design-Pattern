class BasicRamenRecipe:#Abstract class
    
    def __init__(self):
        print("Basic Recipe\n")
    def cookRamen(self):
        self.boilwater()
        self.addRamen()
        self.addons()
        self.wait()
        
    def boilwater(self): #물 끓이기
        print("Boil 550ml of water.")
    
    def addRamen(self): #면, 스프, 후레이크 넣기
        print("Put noodles, Soup base, Flakes in.")
    
    def addons(self): #별도 추가 재료
        pass
    
    def wait(self): #익히기
        print("Cook for 4min 30s.\n")
        
class DadRecipe(BasicRamenRecipe):#Subclass 1
    def __init__(self):
        print("Dad's Recipe\n")
    def addons(self):
        print("Add green onions.")
        print("Add a beaten egg.")
        
class MyRecipe(BasicRamenRecipe): #Subclass 2
    def __init__(self):
        print("My Recipe(best)\n")
    def addons(self):
        print("Add green onions")
        print("Add an egg")
        
    def wait(self):
        print("Cook for 3min 30s\n")

basicRecipe = BasicRamenRecipe()
basicRecipe.cookRamen()

dadRecipe = DadRecipe()
dadRecipe.cookRamen()

myRecipe = MyRecipe()
myRecipe.cookRamen()
    