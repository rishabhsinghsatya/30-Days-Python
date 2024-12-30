# code 1
class Car:
    def __init__(self, brand, model):  # Constructor
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car: {self.brand} {self.model}")


my_car = Car("Toyota", "Corolla")  # Object of the Car class
my_car.display()  # Calls the method of the class


# code 2
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Current balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")


# Creating objects of the BankAccount class
account1 = BankAccount("Alice", 500)
account2 = BankAccount("Bob")

# Performing operations
account1.deposit(200)  # Output: Deposited $200. New balance: $700
account1.withdraw(100)  # Output: Withdrew $100. New balance: $600

account2.deposit(300)  # Output: Deposited $300. New balance: $300
account2.withdraw(400)  # Output: Insufficient funds! Current balance: $300
