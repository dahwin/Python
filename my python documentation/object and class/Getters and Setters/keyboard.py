# plymorphism

from Item import Item

class Keyboard(Item):
  pay_rate =   0.5
  def __init__(self, name:str, price:float, quantity =0, broken_kayboard=0):
        # Call to supeer fuction to have access to all attributes/ method
        super().__init__(
            name,price,quantity
        )
        # Run validations to the recived arguments

        assert broken_kayboard >= 1 , f"borken_car {broken_kayboard} isn't greater than 1"


        # Assing to self object
        self.keyboard_car = broken_kayboard