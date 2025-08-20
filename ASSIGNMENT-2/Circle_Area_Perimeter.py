# Write a Python class named Circle constructed by a radius 
# and two methods which will compute the area and the 
# perimeter of a circle 


import math
class Circle:
    def __init__(self,radius):
        self.r = radius

    def area(self):
        a = math.pi * self.r * self.r
        print(f"Area of circle with radius {self.r} is {a}")

    def perimeter(self):
        p = 2 * math.pi * self.r
        print(f"perimeter of circle with radius {self.r} is {p}")


obj = Circle(2)
obj.area()
obj.perimeter()

obj1 = Circle(11)
obj1.area()
obj1.perimeter()