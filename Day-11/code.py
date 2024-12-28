# Example 1: Basic Exception Handling
try:
    # Taking input from the user
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    # Attempting to divide the numbers
    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    # Handling division by zero
    print("Error: You cannot divide by zero!")

except ValueError:
    # Handling invalid input
    print("Error: Please enter valid numbers.")

# This block will always run
finally:
    print("Thanks for using the program!")

# Example 2: Raising Exceptions
def check_age(age):
    if age < 0:
        # Raising an exception if age is negative
        raise ValueError("Age cannot be negative!")
    return age

try:
    user_age = int(input("Enter your age: "))
    print(f"Your age is: {check_age(user_age)}")
except ValueError as e:
    print(f"Error: {e}")
