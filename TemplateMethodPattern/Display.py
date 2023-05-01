class AbstractDisplay: #Abstract class
    def open(self):
        pass
    
    def textPrint(self):
        pass
    
    def close (self):
        pass
    
    def display(self):
        self.open()
        self.textPrint()
        self.close()
        
class CharDisplay(AbstractDisplay): #Subclass 1
    
    def __init__(self, ch):
        self.ch = ch
        
    def open(self):
        print("<<", end = '')
        
    def textPrint(self):
        print(self.ch, end = '')
        
    def close(self):
        print(">>")
        
class StringDisplay(AbstractDisplay): #Subclass 2
    
    def __init__(self, str):
        self.str = str
        self.size = len(str)
        
    def open(self):
        self.drawLine()
        
    def textPrint(self):
        print("|" + self.str + "|")
        
    def close(self):
        self.drawLine()
        
    def drawLine(self):
        for _ in range(self.size + 2):
            print("+", end = '')
        print()
            
character = CharDisplay("A")
str = StringDisplay("Hello world!")

character.display()
str.display()            
