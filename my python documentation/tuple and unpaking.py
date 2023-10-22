#example of tuple
tupl = ('java','python','c++')
#tupl.index('python')
print(type(tupl))

#paking
#when we creat a tuple , than the way we asssign the value to it , it's called 'paking' a tuple:
fruits = ("apple", "banana", "cherry")

print(fruits)

#unpaking
#but we python we have some strong feature . we are alsoo allowed to extract the values back into variables . This is callledd "unpacking":

bais_of_ra_stb = ('v','jk','jm')
x , y, z = bais_of_ra_stb
print(x)
#unsing Asterisk in unpacking
#if asterisk '*' is added to another variable name than the last ,Python will assign values to the variable until the number of vallluesleft matches the number of variables left.
my_favourite_lan = ('pyhon','java','c++','c','c#','javascript')
(j , k , *d) = my_favourite_lan
print(j)
print(k)
print(d)