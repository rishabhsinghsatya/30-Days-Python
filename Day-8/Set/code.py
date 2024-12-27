fruits = {"apple", "banana", "cherry"}

# Add elements to the set
fruits.add("orange")

# Remove elements from the set
fruits.remove("banana")
print(fruits)

# Set operations: union, intersection, and difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}


# -------------------------------------------------------------- #
# -------   Set Operations with Lists and Dictionaries   ------- #
# -------------------------------------------------------------- #

# Converting a list to a set to remove duplicates
numbers = [1, 2, 3, 3, 4, 5, 1]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Using set operations with dictionaries' keys
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Get keys of dictionaries as sets
keys1 = set(dict1.keys())
keys2 = set(dict2.keys())

# Union, intersection, and difference
print(keys1 | keys2)  # Union
print(keys1 & keys2)  # Intersection
print(keys1 - keys2)  # Difference
