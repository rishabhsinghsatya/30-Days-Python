# Create a tuple
point = (1, 2, 3, 4, 5)
print(type(point))
print(point)

# Access elements
print(point[0])  # First element
print(point[-1])  # Last element
print(point[0:3])

# unpack value into variable
first, second, *other = point
print(first)
print(second)
print(other)
