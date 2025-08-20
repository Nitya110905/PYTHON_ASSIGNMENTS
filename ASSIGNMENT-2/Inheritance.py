# Explain Inheritance in Python with an example? What is init? Or 
# What Is A Constructor In Python? 

# -> Inheritance is a concept of OPPs that allows you to create a new class that inherits the attributes and methods of an existing class.


# -> The __init__ method (short for "initialize") is a special method in Python that serves as the constructor for a class. It is automatically called when you create a new instance (object) of a class.


class Vehicle:
    def __init__(self, brand, year):
        print("Vehicle object created...")
        self.brand = brand
        self.year = year

    def start_engine(self):
        return f"The engine of the {self.brand} is now running."

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        print("Car object created...")
        super().__init__(brand, year)
        
        self.num_doors = num_doors


my_car = Car("Honda", 2025, 4)

print(f"My car is a {my_car.year} {my_car.brand}.")

print(f"It has {my_car.num_doors} doors.")
