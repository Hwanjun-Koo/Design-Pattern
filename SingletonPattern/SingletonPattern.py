class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print('create')
            cls.instance = super(Singleton, cls).__new__(cls)
        else:
            print('recycle')
        return cls.instance

s1 = Singleton()
print(s1)

s2 = Singleton()
print(s1)

print(s1 is s2)