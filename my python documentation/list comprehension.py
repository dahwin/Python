# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#
#Example:
numbers = [200,1,2,44,44,44,5, 6, 66,12,31,223,]
singel = []
for number in numbers:
    if number not in singel:
        singel.append(number)
        print(singel)

