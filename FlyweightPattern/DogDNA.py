class DogBreedDNA:
    def __init__(self, breed, DNA):
        self.breed = breed
        self.DNA =DNA
        
class Dog:
    DNA_table = {}
    @staticmethod
    def addDNA(breed,DNA):
        breed_DNA = DogBreedDNA(breed, DNA)
        Dog.DNA_table[breed] = breed_DNA
        
    def __init__(self,name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        if breed not in Dog.DNA_table:
            print(f"{breed} is not in DNA table. Please add DNA info.")
        
    def __repr__(self):
        return f'{self.name}, {self.age}, {Dog.DNA_table[self.breed].DNA}'
    
Dog.addDNA('Poodle', 'ATAGGCTTACCGATGG..')
Dog.addDNA('Jindo', 'ATAGGCTTACCGATGA..')

choco = Dog('Choco', 2, 'Male', 'Poodle')
Baekgu = Dog('Baekgu', 3, 'Female', 'Jindo')

print(choco)
print(Baekgu)