# Write a Python program to map two lists into a dictionary 


keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

my_dict = dict(zip(keys, values))

print(my_dict)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}