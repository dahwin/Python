#dahyun+darwin = dahwin
from collections import defaultdict
import math
# Create a defaultdict with int as the default factory
word_counts = defaultdict(int)

# Count the frequency of words in a list
word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in word_list:
    word_counts[word] += 1

print(word_counts)  # Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})
import collections
x = dir(math)
print('\n'.join(x))
