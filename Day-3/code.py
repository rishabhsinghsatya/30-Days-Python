# Arithmetic operations
a = 10
b = 3
print("Addition:", a + b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)

# Logical operations
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Membership operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("grape" not in fruits)  # True

# Understand Conditional Statements
    # 1.Use if, elif, and else to control program flow
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


   # Nested if conditions
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")

