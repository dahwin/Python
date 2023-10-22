# Lamda fuction :
# Lamda fuction is fuction written in one line in python.
'''
def celsius_to_fahernheit(celsius):
    fuck = celsius* 33.8
    return fuck

print(celsius_to_fahernheit(100))
'''
#Lamda

calsius_to_f = lambda celsius: celsius* 33.8

print(calsius_to_f(100))


'''
def fahernheit_to_celsius(fahernheit):
    return fahernheit/33.8
print(fahernheit_to_celsius(10000))
'''
farhernheit_to_c = lambda ferhernheit: ferhernheit/33.8
print(farhernheit_to_c(10000))

# Bmi
def BMI(height,weight):
    height = float(input('Enter your height in cm'))
    weight = float(input('Enter your weight in kg'))
    bmi = weight/(height)**2
    if bmi<=18.4:
        print('you are underweight')
    elif bmi <= 24.9:
        print('you are healthy')
    elif bmi <= 34.9:
        print('You are severely over weight')
    elif bmi <= 39.9:
        print('you are obese')
    else:
        print('your are severely obese')
    return print(bmi)

print(BMI(1.78,70))
