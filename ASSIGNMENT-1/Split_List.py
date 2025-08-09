# Write a Python program to split a list into different variables.
# You can split a list into different variables in Python using a technique called iterable unpacking.

user_data = ['John Doe', 34, 'New York']

name, age, city = user_data

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

numbers = [10, 20, 30, 40, 50]

# The variable with the * will always be assigned a new list containing the "leftover" items.
first, *rest = numbers

print(f"The first number is: {first}")
print(f"The rest of the numbers are: {rest}")