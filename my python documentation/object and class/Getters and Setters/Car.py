from Item import Item

class Car(Item):

    def __init__(self,name:str, price:float,  quantity =0,borken_car=0):
        # Call to supeer fuction to have access to all attributes/ method
        super().__init__(
            name,price,quantity
        )
        # Run validations to the recived arguments

        assert borken_car>=1 ,f"borken_car {borken_car} isn't greater than 1"


        # Assing to self object
        self.borken_car = borken_car