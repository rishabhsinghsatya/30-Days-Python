# Define a function
def greet():
    print("Hello, welcome to Python learning!")
# Call the function
greet()


# Function with Parameters
def intro(name):
    print(f"Hello, {name}! How are you today?")
intro("Joe")


# Function with Return Values
def add(a, b):
    return a + b
result = add(10, 20)
print(result)


# Default Parameters
def learn(language="python"):
    print(f"Today we learn, {language}")
learn()
learn("javascript")


# Local vs. Global Scope
# Global variable
name = "global variable"
def local():
    # Local variable
    name = "local variable"
    print(f"Inside function: {greeting}")
local()
print(f"Outside function: {name}")
