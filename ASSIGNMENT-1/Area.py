# Write a Python program to calculate the area of a trapezoid 

a = float(input("Enter the length of the first parallel side (a): "))
b = float(input("Enter the length of the second parallel side (b): "))
height = float(input("Enter the height of the trapezoid: "))

area = ((a + b) * height) / 2
print(f"Area of the trapezoid: {area}")

#  Write a Python program to calculate the area of a parallelogram

base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = base * height
print(f"Area of the parallelogram: {area}")

# Write a Python program to calculate surface volume and area of a cylinder 
import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = 2 * math.pi * radius * (height + radius)
volume = math.pi * radius ** 2 * height

print(f"Surface Area of the cylinder: {surface_area}")
print(f"Volume of the cylinder: {volume}")


