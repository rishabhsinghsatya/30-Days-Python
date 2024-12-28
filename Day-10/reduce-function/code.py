# The reduce() function from the functools module applies a function of two arguments cumulatively to the items in an iterable, from left to right, so as to reduce the iterable to a single value.

from functools import reduce

# Using reduce to multiply all numbers in a list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24