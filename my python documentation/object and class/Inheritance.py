import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name:str, price:float,  quantity =0):
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
    @classmethod
    def instantiate_from_csv(cls):
        with open('csv.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name= item.get('price'),
                    price= float(item.get('price')),
                    quantity=int(item.get('quantity'))

                )
    @staticmethod
    def is_integer(num):
         #We will count out the floats that are point zero
         #For i.e: 5.0,10.0
         if isinstance(num,float):
             # Count out the floats that are point zero
             return num.is_integer()
         elif isinstance(num,int):
             return  True
         else:
             return  False



    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


class Car(Item):
    all = []
    def __init__(self,name:str, price:float,  quantity =0,borken_car=0):
        # Run validations to the recived arguments
        assert price>= 1,f"Price{price}is can't be zero!"
        assert quantity>=1 ,f"Quantity {quantity} isn't greater than 1"
        assert borken_car>=1 ,f"borken_car {borken_car} isn't greater than 1"


        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.borken_car = borken_car
        #Action to execut
        Car.all.append(self)


car1 = Car('Toyta',50000,10,1)
car2 = Car('Ford',60000,10,1)

print(Car.all)
print(Item.all)

print(car1.calulate_total_price())

