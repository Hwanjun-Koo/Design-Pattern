class MyInt(type):
    
    def __call__(cls, *args, **kwds):
        print("Myint", args)
        print("Now dow whatever you want with these objects ")
        return type.__call__(cls, *args, **kwds)
        
class int(metaclass = MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
myint = int(1, 2)


