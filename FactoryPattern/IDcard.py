class Product:
    def use(self):
        pass

class Factory:
    def create(self, owner) -> Product:
        p = self.createProduct(owner)
        self.registerOwner(p)
        return p
    
    def createProduct(self, owner) -> Product:
        pass
    
    def registerOwner(self, product):
        pass
    
class IDCard(Product):
    def __init__(self,owner):
        self.owner = owner
        print(self.owner + " 의 카드를 만듭니다.")
        
        
    def use(self):
        print(self.owner, "의 카드를 사용합니다.")
    
    def getOwner(self):
        return self.owner
    
class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []
        
    def createProduct(self, owner):
        return IDCard(owner)
    
    def registerOwner(self, product):
        self.owners.append(product.getOwner())
        
    def getOwners(self):
        return print(self.owners)
    
factory = IDCardFactory()
card1 = factory.create("a")
card2 = factory.create("b")

card1.use()
card2.use()
factory.getOwners()
