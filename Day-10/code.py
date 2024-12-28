# ------------------------------------ #
# -------   Lambda Functions   ------- #
# ------------------------------------ #
double = lambda x: x * x
print(double(5))

add = lambda x, y: x + y
print(add(10, 20))


# ---------------------------------- #
# -------   map() Function   ------- # square numbers in a list
# ---------------------------------- #
numbers = [1, 2, 3, 4, 5, 6]  # use this list in all example
# ---------------------------------- #
def square(x):
    return x * x
data = list(map(square, numbers))
print(data)  # [1, 4, 9, 16, 25, 36]

# OR

square_number = map(lambda x: x * x, numbers)
print(list(square_number))  # [1, 4, 9, 16, 25, 36]


# ------------------------------------- #
# -------   filter() Function   ------- # Using filter to find even numbers
# ------------------------------------- #
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # [2, 4, 6]


# ------------------------------------------ #
# -------   Higher-Order Functions   ------- #
# ------------------------------------------ #
# A higher-order function that takes a function and applies it to two numbers
def apply_function(func, a, b):
    return func(a, b)


result = apply_function(lambda x, y: x * y, 5, 6)
print(result)  # Output: 30


# ------------------------------------------ #
# -------   Closures   ------- #
# ------------------------------------------ #
# function that remembers the multiplier
def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply

# Creating a closure with a factor of 2
double = multiplier(2)
print(double(4))  # Output: 8
