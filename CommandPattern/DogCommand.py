from typing import List
class Command:
    def execute(self):
        pass
class Dog:
    
    def sit(self):
        print("Dog sat down")
        
    def fetch(self):
        print("Dog fetched the ball")
        
class DogCommand(Command):
    def __init__(self, dog:Dog, commands:List[str]):
        self.dog = dog
        self.commands = commands
        
    def execute(self):
        for command in self.commands:
            if command == 'sit':
                self.dog.sit()
            elif command == 'fetch':
                self.dog.fetch()
                
class Invoker:
    def __init__(self):
        self.command_list = []
        
    def addCommand(self, command:Command):
        self.command_list.append(command)
        
    def runCommands(self):
        for command in self.command_list:
            command.execute()
            
jindo = Dog()
dog_command = DogCommand(jindo, ['sit', 'fetch', 'fetch'])
invoker = Invoker()
invoker.addCommand(dog_command)
invoker.runCommands()