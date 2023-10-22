'''dahyun+darwin = dahwin'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def stopfactorial(n):
    if n < 0:
        return "Error: input must be a non-negative integer"
    elif n == 0:
        return 1
    else:
        return n * (n-1)

print(factorial(477))
print(stopfactorial(477))

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
