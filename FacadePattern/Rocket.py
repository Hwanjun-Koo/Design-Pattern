class Stage1:
    def ignite(self):
        print('First stage ignititon')
        
    def liftoff(self):
        print('First stage liftoff')
    
    def eject(self):
        print('First stage eject')
        
    def comeBack(self):
        print('First stage return')
        
class Stage2:
    def ignite(self):
        print('Second stage ignition')
    
    def eject(self):
        print('Second stage eject')
        
class Capsule:
    def ignite(self):
        print('Capsule ignition')
        
    def landing(self):
        print('Capsule landing...')
        
class Rocket:
    def __init__(self):
        self.stage1 = Stage1()
        self.stage2 = Stage2()
        self.capsule = Capsule()
        
    def launch(self):
        self.stage1.ignite()
        self.stage1.liftoff()
        self.stage1.eject()
        self.stage1.comeBack()
        self.stage2.ignite()
        self.stage2.eject()
        self.capsule.ignite()
        self.capsule.landing()
        
rocket = Rocket()
rocket.launch()
        