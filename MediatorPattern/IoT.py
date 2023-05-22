class Mediator:
    def notify(self, signal: str):
        pass
    
class Clock:
    def setMediator(self, mediator: Mediator):
        self.mediator = mediator
    def Alarm(self):
        print("Alarm on")
        self.mediator.notify('AlarmOn')
        
class Light:
    def setMediator(self, mediator: Mediator):
        self.mediator = mediator
    def On(self):
        print("Light On")
    def Off(self):
        print("Light Off")
        self.mediator.notify('LightOff')
    
class Speaker:
    def setMediator(self, mediator:Mediator):
        self.mediator = mediator
    def On(self):
        print("Speaker On")
    def Off(self):
        print("Speaker Off")

class IOT(Mediator):
    def __init__(self, clock, light, speaker):
        self.clock = clock
        self.light = light
        self.speaker = speaker
        
    def notify(self, signal: str):
        if signal == 'AlarmOn':
            self.speaker.On()
            self.light.On()
            
        elif signal == 'LightOff':
            self.speaker.Off()
            
clock = Clock()
light = Light()
speaker = Speaker()

mediator = IOT(clock, light, speaker)

clock.setMediator(mediator)
light.setMediator(mediator)
speaker.setMediator(mediator)

clock.Alarm()
light.Off()