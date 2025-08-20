# Write a Python class named Rectangle constructed by a length 
# and width and a method which will compute the area of a 
# rectangle 


class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        area = self.length * self.width
        print(f"Your Rectangle with length : {self.length} and width : {self.width} is {area}")

obj = Rectangle(10,20)
obj.area()
        