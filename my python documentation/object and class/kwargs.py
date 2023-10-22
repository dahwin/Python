# ** kwargs = parameter that will peck all arguments into a dictionart
#             useful so that a fucntion can accept a varying amount of keyword argument
def name(first,last):
    print('hello world'+first+" "+last)

name(first=" dawin",last=" darwin")

def hello(**kwargs):
    #print('hello world'+ kwargs['first']+ " " +kwargs['last'])
    print('Hellow', end=' ')
    for key,value in kwargs.items():
        print(value,end=' ')

hello(first="dawin",koeean='kim',middle='dahyun',last="darwin")