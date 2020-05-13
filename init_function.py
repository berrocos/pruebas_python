class Person():
    def __init__(self,name):
        self.name=name
    
    def say_hi(self):
        print('Hello, mi nombre es',self.name)


p=Person('Andres')
p.say_hi()