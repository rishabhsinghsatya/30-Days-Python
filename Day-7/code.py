message = "hello python programmer"

print(len(message))
print(message[0])  # h
print(message[-1])  # r

print(message[0:4])  # hell
print(message[:7])  # hello p

# ----------string methods----------#
# Strip whitespace
print(message.strip())

# Convert to uppercase and lowercase
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())

# Replace text
print(message.replace("Python", "Coding"))

# Split and join
words = message.split()  # Split into a list of words
print("Words:", words)
print("-".join(words))


#----------string formatting----------#
# Variables
name = "john"
age = 25

# Formatted string
greeting = f"My name is {name} and I am {age} years old."
print(greeting)

# Expression evaluation inside f-strings
x, y = 5, 10
result = f"The sum of {x} and {y} is {x + y}."
print(result)
