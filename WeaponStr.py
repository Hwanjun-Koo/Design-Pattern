from abc import *

class Weapon(metaclass = ABCMeta):
    @abstractclassmethod
    def offensive(self):
        pass
    
class Sword(Weapon):
    def offensive(self):
        print("Slash")
        
class Shield(Weapon):
    def offensive(self):
        print("Rush")

class CrossBow(Weapon):
    def offensive(self):
        print("Flame Shot")

class TakeWeaponStrategy:
    
    def __init__(self):
        self.weapon = 0
        
    def setWeapon(self, weapon:Weapon):
        self.weapon = weapon
    
    def attack(self):
        self.weapon.offensive()
    
hand = TakeWeaponStrategy()

hand.setWeapon(Sword())
hand.attack()

hand.setWeapon(Shield())
hand.attack()


