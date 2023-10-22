#__init__  is a maker of constructor
class Ratul_class:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def open(self):
        print('open')
    def close(self):
        print('close')
number = 4, 5, 3,5
fuc1 = Ratul_class(14,20)
print(fuc1.open())
print(fuc1.x)

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print('talk')

point1 = Person('kim Dahyun')
print(point1.name)