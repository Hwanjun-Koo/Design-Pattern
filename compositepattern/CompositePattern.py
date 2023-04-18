class Component:
    def fn(self):
        pass
class Leaf(Component):
    def fn(self):
        print('leaf')
class Composite(Component):
    def __init__(self):
        self.components = []
    def add(self, component:Component):
        self.components.append(component)
    def fn(self):
        print('composite')
        for component in self.components:
            component.fn()
            
compst1 = Composite()
compst1.add(Leaf())
compst1.add(Leaf())

compst0 = Composite()
compst0.add(Leaf())
compst0.add(compst1)

compst0.fn()