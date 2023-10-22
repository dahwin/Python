def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
       if number > maximum:
           maximum = number
           return maximum

o = 6 , 88 , 4
maxi = find_max(o)
print(maxi)