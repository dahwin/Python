from Item import Item
from Car import Car

item1 = Item('MyItem',740,4)
item1.name = 'fuckh'
print(item1.name)
print(item1.calulate_total_price())

print(item1.name)

print(item1.price)

item1.apply_increment(0.2)

print(item1.price)

from keyboard import  Keyboard

item2 = Keyboard('dawin',1000,10,1)
print(item2.all)