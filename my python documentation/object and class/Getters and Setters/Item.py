import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name:str, price:float,  quantity =0):
        # Run validations to the recived arguments
        assert price>= 1,f"Price{price}is can't be zero!"
        assert quantity>=1 ,f"Quantity {quantity} isn't greater than 1"

        # Assing to self object
        self._name = name
        self.__price = price
        self.quantity = quantity
        #Action to execut
        Item.all.append(self)

    # This is encapsulation

    @property
    def price(self):
        return self.__price


    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decortor = Read-Only Attribute
    def name(self):
        return  self._name
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise  Exception("The name is too long")


    def calulate_total_price(self):
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open('csv.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name= item.get('name'),
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
        return f"Item('{self.name}',{self.__price},{self.quantity})"

    @property
    def Love_of_dahyun(self):
        return 'I love u dahyun so much🥰'