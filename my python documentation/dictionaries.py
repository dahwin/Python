ratul = {
    'name' : 'ratul',
    'location' : 'kawnia first lane , barisal',
    'country' : 'bangladesh',
    'education': 'computer science',
    'lady love and sister': 'kim dahyun',
    'height' : '5 feet 7 inch' ,
     'age' : '18'
}

print(ratul['lady love and sister'])

#.get
#there is also a method called .get that will give you the same result:

print(ratul.get('education'))

#.key
# the .key method will return a list of all the keys in the dictionary

x = ratul.keys()
print(x)

#.values
# the .values method will return a list osf all the values in the dictionary

print(ratul.values())

#.items
# the .items method will return each item in a dictionary , as tuples in a list .

print(ratul.items())

#.clear
# it will remove all the items from dictionary and give u 'None' object
print(ratul.clear())

print(ratul.copy())
#.pop
# this method removes the item with the specified key name:
#ratul.pop('age')

#.update
#the .update method will update dictionary with the items from the given argument.
#The argument must be a dictionary , or an iterable object with : calue pairs

ratul.update({"age": 20})
print(ratul)



