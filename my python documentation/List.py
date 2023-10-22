#add  item on list
#.append
number = [1,2,44, 6, 66,12,31,223,]
number.append(5)
print(number)
#Add the elements of a list (or any iterable), to the end of the current list
#.extend
#it only can add string value
number = [1,2,44, 6, 66,12,31,223,]
number.extend('fff')
print(number)

bts = ['blood sewat and tears' , 'begin' , 'singularity']
bts.extend("cyper killer")
print(bts)



#.replace
#it can replace item from a list/varriable[]
number = [1,2,44, 6, 66,12,31,223,]
number[3] = 5
print(number)
fruit= ['Mango','Apple','Jackfruite','Banana']
fruit[1:3] = 'Berry' , 'Leamon'
print(fruit)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)




#.insert
#insert item in the specipic point
number = [1,2,44, 6, 66,12,31,223,]
number.insert(5,666)
print(number)




#.remove
#it use for removing object from a list
number = [1,2,44, 6, 66,12,31,223,]
number.remove(6)
print(number)

#loop list
number = [1,2,44, 6, 66,12,31,223,]
number.remove(6)
print(number)



#list comprhension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

numbers = [1,2,44, 6, 66,12,31,223,]
singel = []
for number in numbers:
    if number not in singel:
        print(singel)



#sort List objects have a sort() method that will sort the list alphanumerically, ascending ,descending, by default:

number = [1,2,44, 6, 66,12,31,223,]
number.sort()
print(number)
number = [1,7,5,2,44, 6, 66,12,31,223,]
number.sort()
number.reverse()
print(number)



#.copy list
#it used to copying information from one list to another list

number = [1,2,44, 6, 66,12,31,223,]
rebmun = number.copy()
print(number)

#.join list
# this is the way to join , orf concatenate, two or more lists in python
number = [1,2,44, 6, 66,12,31,223,]
addition_tow_list = number + rebmun
print(addition_tow_list)




#list method
number = [1,2,44, 6, 66,12,31,223,]
number.remove(6)
print(number)






#.pop
#Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)




#.index
#The index() method returns the position at the first occurrence of the specified value.
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


#.count
# this .count methon return the number of element with the specified value
tupl = ('java','python','c++')
p=tupl.count('java')
print(p)

