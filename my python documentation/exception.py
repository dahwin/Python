# it usually used to run code without showing syntax error
try:
    type_your_age = int(input('enter your age:'))
    print(type_your_age)
except ValueError:
    print('value error')

except ZeroDivisionError:
    print('invalid value')

except OverflowError:
    print('invalid value')