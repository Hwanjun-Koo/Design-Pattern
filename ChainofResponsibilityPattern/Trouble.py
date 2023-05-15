class Trouble:
    
    def __init__(self, number):
        self.number = number
        
    def getNumber(self):
        return self.number
    
class Support:
    
    def __init__(self, name):
        self.name = name
        self.next = None
        
    def setNext(self, next):
        self.next = next
        return next
    
    def support(self, trouble:Trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self.next != None:
            self.next.support(trouble)
        else:
            self.fail(trouble)
            
    def resolve(self, trouble):
        pass
    
    def done(self, trouble):
        print(str(trouble.getNumber()) + " is resolved by " + str(self.name))
        
    def fail(self, trouble):
        print(str(trouble.getNumber()) + " cannot be resolved..")
        
class Nosupport(Support):#출입창구
    
    def __init__(self, name):
        super().__init__(name)
    
    def resolve(self, trouble:Trouble):
        return False

class OddSupport(Support): #홀수번호 처리
    
    def __init__(self, name):
        super().__init__(name)
        
    def resolve(self, trouble:Trouble):
        if trouble.getNumber() % 2 == 1:
            return True
        else:
            return False
        
class LimitSupport(Support): #특정 숫자보다 작은 수 처리
    
    def __init__(self, name, limit):
        super().__init__(name)
        self.limit = limit
            
    def resolve(self, trouble:Trouble):
        if trouble.getNumber() < self.limit:
            return True
        else:
            return False
        
class SpcialSupport(Support):
    
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number
        
    def resolve(self, trouble:Trouble):
        if trouble.getNumber() == self.number:
            return True
        else:
            return False
        
alice = Nosupport("Alice")
bob = LimitSupport("Bob", 100)
charlie = SpcialSupport("Charlie", 429)
diana = LimitSupport("Diana", 200)
elmo = OddSupport("Elmo")
fred = LimitSupport("Fred", 300)

alice.setNext(bob).setNext(charlie).setNext(diana).setNext(elmo).setNext(fred)

for i in range(1, 500, 33):
    alice.support(Trouble(i))
        