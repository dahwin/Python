class Item:
    # this is root of methods or function
    def calulate_total_price(self, x , y):
        return x * y
item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 4
price = item1.calulate_total_price(item1.price,item1.quantity)

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 5
price1 = item2.calulate_total_price(item2.price,item2.quantity)

print(price,price1)