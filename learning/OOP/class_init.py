class Person:
    def __init__(self, name):
        self.name = name
        print('привет. чо как?', self.name)
    def sayHi(self):

p = Person('Swaroop')
p.sayHi()
