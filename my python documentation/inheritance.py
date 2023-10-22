#Inheritance allows us to define ackass that lagacies all rhe methods ans properties from another class .
#parent class is the class being inherited from , also called base class.
#

class exampele_inheritance :
    x = 9,3,2,4,5,2,2

objectp = exampele_inheritance()
print(objectp.x)

class dahyun(exampele_inheritance):
    pass

class Kim_dahyun(exampele_inheritance):
    truth = 'ratul love dahyun'

objectr = Kim_dahyun()
print(objectr.truth)
print(objectr.x)
