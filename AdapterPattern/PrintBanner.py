#상속 방식
class Banner():
    
    def __init__(self, word):
        self.word = word
        
    def withParen(self):
        print("(" + self.word + ")")
        
    def withAster(self):
        print("*" + self.word + "*")
        
class Print():
    
    def printWeak(self):
        pass
    def printStrong(self):
        pass 
    
class PrintBanner(Banner, Print): #상속을 2개를 받았지만 앞에있는 Banner클래스를 먼저 사용
    
    def __init__(self, word):
        super(PrintBanner, self).__init__(word)#Banner 클래스임을 알려줌
        
    def printWeak(self):
        self.withParen()
        
    def printStrong(self):
        self.withAster()
        
pb = PrintBanner("Hello")
pb.printWeak()
pb.printStrong()