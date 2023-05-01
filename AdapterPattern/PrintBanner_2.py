class Banner(): # 제공되는 것(Adaptee)
    
    def __init__(self, word):
        self.word = word
        
    def withParen(self):
        print("(" + self.word + ")")
        
    def withAster(self):
        print("*" + self.word + "*")
        
class Print(): #필요한 것(Target)
    
    def printWeak(self):
        pass
    def printStrong(self):
        pass
    
class PrintBanner(Print):
    
    def __init__(self,word):
        self.banner = Banner(word) #위임 발생 부분
        
    def printWeak(self):
        self.banner.withParen()
        
    def printStrong(self):
        self.banner.withAster()
        
pb = PrintBanner("Hello")
pb.printWeak()
pb.printStrong()
    
