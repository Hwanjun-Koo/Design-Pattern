from abc import*
class Robot(metaclass = ABCMeta):
    @abstractmethod
    def action(self):
        pass
    
class Walk(Robot):
    def action(self):
        print("Walking....")
        
class Run(Robot):
    def action(self):
        print("Running!")
        
class Gun(Robot):
    def action(self):
        print("Headshot!")

class Rocket(Robot):
    def action(self):
        print("BOOM!")
        
class Action:
    def __init__(self):
        self.robot = 0
        
    def setAction(self, robot:Robot):
        self.robot = robot

    def action(self):
            self.robot.action()

        
        

action = Action()

action.setAction(Walk())
action.action()
action.setAction(Run())
action.action()

action.setAction(Gun())
action.action()
action.setAction(Rocket())
action.action()
