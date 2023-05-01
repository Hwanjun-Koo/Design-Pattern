class Power:
    def powerUp(self):
        pass
    
    def powerDown(self):
        pass
    
    
class Engine(Power):
    def powerUp(self):
        print('Starting Engine..')
        
    def powerDown(self):
        print('Turning off..')
        
class Motor(Power):
    def powerUp(self):
        print('Starting Motor..')
        
    def powerDown(self):
        print('Turning off..')
        
class Car:
    def __init__(self, power:Power):
        self.power = power
        
    def drive(self):
        self.power.powerUp()
    
    def stop(self):
        self.power.powerDown()

class Sedan(Car):
    
    def drive(self):
        self.power.powerUp()
        print('Now you can drive a Sedan.')
        
class SUV(Car):
    
    def drive(self):
        self.power.powerUp()
        print('Now you can drive a SUV.')
        
class Truck(Car):
    
    def drive(self):
        self.power.powerUp()
        print('Now you can drive a Truck.')


    
sedan = Sedan(Engine())
sedan.drive()