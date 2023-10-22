# *args = parameter that will pack all arguments into a tuple
#       useful so that a fuction can accept a varying amount of arguments

def add(num1,num2):
    sum = num1 + num2
    return sum
print(add(1,2))

def addition(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(addition(2,3,41,1,2233,4))