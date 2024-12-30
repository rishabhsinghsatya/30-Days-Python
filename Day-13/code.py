class Car:
    def __init__(self, brand, model):  # Constructor
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car: {self.brand} {self.model}")


my_car = Car("Toyota", "Corolla")  # Object of the Car class
my_car.display()  # Calls the method of the class
