# How to Define a Class in Python? What Is Self? Give An 
# Example Of A Python Class 

# -> A class in Python is defined using the class keyword. A class is a blueprint for creating objects, bundling together data (attributes) and functions that operate on that data (methods).

# -> Self is a conventional name for the first parameter of a method in a class. It represents the instance of the class itself.

# Use the 'class' keyword followed by the class name (in PascalCase)
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0  
    def accelerate(self, amount):
        """Increases the car's speed."""
        self.speed += amount
        print(f"The {self.color} {self.brand} accelerates to {self.speed} km/h.")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"The {self.color} {self.brand} slows down to {self.speed} km/h.")

    def get_status(self):
        return f"This is a {self.color} {self.brand} currently moving at {self.speed} km/h."

my_car = Car("Toyota", "blue")
friends_car = Car("Ford", "red")

my_car.accelerate(50)
friends_car.accelerate(70)
my_car.brake(20)

print("\n--- Status Report ---")
print(my_car.get_status())
print(friends_car.get_status())