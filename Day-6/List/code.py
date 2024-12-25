letters = ["a", "b", "c"]
print(letters)  # ['a', 'b', 'c']

matrix = [[0, 1], [2, 31]]
print(matrix)  # [[0, 1], [2, 31]]

zeros = [0] * 5
combined = zeros + letters
print(combined)  # [0, 0, 0, 0, 0, 'a', 'b', 'c']

numbers = list(range(20))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

chars = list("Hello World")
print(chars)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(len(chars))  # 11

#-------------------------------------------#
fruits = ["apple", "banana", "cherry"]
print(fruits)

# access elements
print(fruits[0])
print(fruits[-1])

# slicing
print(fruits[0:2])

# adding elements
fruits.append("orange")  # Add to the end
print(fruits)
fruits.insert(1, "mango")
print(fruits)

# removing elements
fruits.pop()  # Remove the last element
fruits.remove("banana")
print(fruits)

#----------- List Methods
numbers = [5, 3, 8, 6]
numbers.sort()  # Sort in ascending order
print(numbers)

numbers.reverse()  # Reverse the list
print(numbers)

print(len(numbers))  # Length of the list


# ------------------List unpacking
sequence = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, *other = sequence
print(sequence)
print(first)
print(second)
print(other)
