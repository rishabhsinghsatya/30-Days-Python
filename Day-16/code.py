# -------------------------------------------------------------------------------------------------- #
# In Python, comprehensions are concise and readable constructs for creating collections like lists, dictionaries, and sets in a single line using an expression, a loop, and optional conditions.
# Benefits of Comprehensions:
#           Conciseness: One-liners make code more compact.
#           Readability: Clear intent when used appropriately.
#           Performance: Often faster than equivalent loops due to optimized C-level execution in Python.
# -------------------------------------------------------------------------------------------------- #

# List comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)  # [2, 4, 6, 8, 10]


# Dictionary Comprehensions
square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)

filtered_dict = {k: v for k, v in square_dict.items() if k > 2}
print(filtered_dict)


# Set Comprehensions
square_set = {x**2 for x in range(1, 6)}
print(square_set)

unique_vowels = {char for char in "comprehensions" if char in 'aeiou'}
print(unique_vowels)

