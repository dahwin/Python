# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(f"Hello, my name is {self.name}.")
#
#
# class Child(Parent):
#     def greet(self):
#         super().greet()  # Call greet() method in the parent class
#         print("How are you doing today?")


class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent initialized.")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(age)
        print("Child initialized.")


# c = Child("Alice")
# c.greet()
c = Child('dahyun',24)