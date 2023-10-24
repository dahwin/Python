class MyClass:
    class_variable = 0  # Class variable shared by all instances

    def __init__(self, value):
        self.instance_variable = value  # Instance-specific variable

    @classmethod

    def increment_class_variable(clss):
        clss.class_variable += 1

    def display_values(self):
        print(f"Instance Variable: {self.instance_variable}")
        print(f"Class Variable: {MyClass.class_variable}")

# Create instances of the class
obj1 = MyClass(10)
obj2 = MyClass(20)
obj3 = MyClass(30)
# Access class method using the class
MyClass.increment_class_variable()

# Access class method using an instance
obj1.increment_class_variable()
obj2.increment_class_variable()
# Display values
obj1.display_values()
obj2.display_values()
obj3.display_values()
