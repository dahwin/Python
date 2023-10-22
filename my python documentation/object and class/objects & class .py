# what is object in programming?:
#In computer science object is data or code as like varriable , data sturcture or method etc. As region of value memory ,they contain value and refarence
# by idetifier . object can be combinition of varriable , function and data structure :in particular in class-based variations of the paradigm
# it refers to a particular instance of a class.
#what is object oriented programming?:
#OOP (Object-oriented- programming) is a programming paradigm based on "object". A common feature of objects is that procedures (or methods) are attached to them and cana acess and modify the object's data fields.

#Object: python is a object oriented programming language . Almost everything in python is an object m with its properties and methods .
#Class : A class is like an object constuctor or object builder or a 'blueprint' for creating objects . Class is basically used to create an object .

class example_class:
    x = 666
    y = 'dahyun'

p = example_class
print(p.x)
#next


class Point:
    def move(self):
        print("move")
    def draw(self):
        print('draw')
ratul = Point()
print(ratul.move())

point1 = Point()
point1.s = 98
point1.j = 32
point1.draw()
print(point1.s, point1.j)

point2 = Point()
point2.s = 76
point2.j = 97
point2.move()
print(point2.s)

