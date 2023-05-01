import time
from abc import*
from asyncio.windows_events import NULL

class Printable(metaclass = ABCMeta):
    
    def __init__(self):
        self.name = ""
        
    @abstractmethod
    def setPrinterName(self):
        pass
    
    @abstractmethod
    def getPrinterName(self):
        pass
    
    @abstractmethod
    def printText(self):
        pass
    
class Printer(Printable):
    
    def __init__(self, name):
        self.name = name
        self.heavyJob("Printer 의 인스턴스 " + self.name + " 을 생성중..")
        
    def setPrinterName(self,name):
        self.name = name
        
    def getPrinterName(self):
        return self.name
    
    def printText(self, msg):
        print("==" + self.name + "==", end = ": ")
        print(msg)
        
    def heavyJob(self, msg):
        print(msg)
        
        for i in range(5):
            time.sleep(1)
            
        print("완료")
        
class PrinterProxy(Printable):
    
    def __init__(self, name):
        self.name = name
        self.real = NULL
        
    def realize(self):
        if self.real == NULL:
            self.real = Printer(self.name)
            
    def setPrinterName(self, name):
        if self.real != NULL:
            self.real.setPrinterName(name)
            
        self.name = name
    
    def getPrinterName(self):
        return self.name
    
    def printText(self, msg):
        self.realize()
        self.real.printText(msg)
        
p = PrinterProxy("Vostok")
print(p.getPrinterName() + " 에서 교신을 시도합니다.")
p.setPrinterName("Mercury")
print("현재 " + p.getPrinterName() + " 와 교신중입니다.")
p.printText("Hello! How are you?")
p.printText("Can you hear me?")        

p.setPrinterName("Apollo")            
print(p.getPrinterName() + " 와 교신을 시도합니다.")
p.printText("We successfully landed on the moon.")