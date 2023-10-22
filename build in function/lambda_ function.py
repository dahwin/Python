sum = lambda x, y: x + y
print(sum(3, 4)) # Output: 7



my_list = [(1, 4), (2, 1), (3, 2), (4, 3)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list) # Output: [(2, 1), (3, 2), (4, 3), (1, 4)]

lst = ['apple', 'banana', 'pear', 'orange', 'kiwi']
lst_sorted = sorted(lst, key=lambda x: len(x))
print(lst_sorted)  # ['kiwi', 'pear', 'apple', 'banana', 'orange']


lst = [(3, 2), (1, 4), (4, 3), (2, 1)]
lst_sorted = sorted(lst, key=lambda x: x[0], reverse=True)
print(lst_sorted)  # [(4, 3), (3, 2), (2, 1), (1, 4)]

lst = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
lst_sorted = sorted(lst, key=lambda x: x['age'])
print(lst_sorted)  # [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    square = (lambda x: x*x)(num)
    squares.append(square)

print(squares)
