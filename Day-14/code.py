# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def sound(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def sound(self):
        return f"{self.name} says Meow!"


# Polymorphism
def animal_sounds(animal):
    print(animal.sound())


# Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


# `super()` usage
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)  # Call parent class constructor
        self.can_fly = can_fly

    def sound(self):
        return f"{self.name} chirps!"


# Testing the code
if __name__ == "__main__":
    # Inheritance Example
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    # Polymorphism Example
    animal_sounds(dog)  # Buddy says Woof!
    animal_sounds(cat)  # Whiskers says Meow!

    # Encapsulation Example
    account = BankAccount("John", 1000)
    account.deposit(500)  # 500 deposited. New balance: 1500
    account.withdraw(300)  # 300 withdrawn. Remaining balance: 1200
    print("Balance:", account.get_balance())  # Balance: 1200

    # Using `super()` Example
    bird = Bird("Sparrow", True)
    print(bird.sound())  # Sparrow chirps!
