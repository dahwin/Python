# parameter : parameter is the variable listed inside the paretheses in the function definition.
# A argument is the value that are sent ti the function when it is called .
def add(a,b):
    return a+b
print(add(5,666))

#in this case /
# here , the parameters are a and b , and the arguments being passed through are 5 and 666.
#since python is a dynamically typed language , we do not need to declare the tyoes of the parameters when declaring a function
#(unlike in other language such as c) . thus we can not control what exact type is passed through as an argument to the function.
#for example , in the above fuction , we could do add ('hello', 'hi' ).
