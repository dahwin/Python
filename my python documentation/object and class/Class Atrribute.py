'''
Class Attribute
A class attribute is a python variable that belongs to a class rather than
a partucular object

class ExampleClass(object):
  class_attr = 0
'''
# class Item:
#     pay_rate = 0.8 # The pay rate after 20% discount
#     def __init__(self,name:str, price:float,  quantity=0):
#         # Run validations to the recived arguments
#         assert price>= 1,f"Price{price}is can't be zero!"
#         assert quantity>=1 ,f"Quantity {quantity} isn't greater than 1"

# Assing to self object

#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#
#     def calulate_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#
# item1 = Item("Phone",100 ,5)
# item1.apply_discount()
#
#
# item2 =Item('Laptop',1000,6)
# item2.pay_rate = 0.7
# item2.apply_discount()
#
# print(item1.price)
# print(item2.price)
#



'''print(Item.__dict__)
'''

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name:str, price:float,  quantity=0):
        # Run validations to the recived arguments
        assert price>= 1,f"Price{price}is can't be zero!"
        assert quantity>=1 ,f"Quantity {quantity} isn't greater than 1"

        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        #Action to execut
        Item.all.append(self)


    def calulate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

item1 = Item('Phone',100,10)
item2 = Item('Laptop',1500,20)
item3 = Item('Iphone',1000,10)
item4 = Item('Mouse',50,10)
item5 = Item('Keyboard',75,10)

# for inste in Item.all:
# # #     print(instance.name)anc

print(Item.all)

print(item1.calulate_total_price())