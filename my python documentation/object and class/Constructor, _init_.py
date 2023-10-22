# class Item:
#     def __init__(self,name):
#         print(f"i am god:{name}")
#         self.name = name
#
#     def calulate_total_price(self, x,y):
#         return x * y
#
# item1 = Item("Phone")
# item1.name = "phone"
# item1.price = 100
# item1.quantity = 4
#
# item2 = Item('Loptop')
# item2.name = Item('Laptop')
# item2.price = 1000
# item2.quantity = 5

class Item:
    def __init__(self,name:str, price:float,  quantity=0):
        # Run validations to the recived arguments
        assert price>= 1,f"Price{price}is can't be zero!"
        assert quantity>=1 ,f"Quantity {quantity} isn't greater than 1"
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"i am god:{name}")
        self.name = name

    def calulate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone",100 ,5)
item2 =Item('Laptop',1000,6)

print(item1.calulate_total_price())
print(item2.calulate_total_price())