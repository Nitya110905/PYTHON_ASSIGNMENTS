# Write a Python program to print all unique values in a dictionary.

d = {'a' : 1 , 'b' : 2 , 'c' : 10 , 'd' : 5 , 'e' : 10 , 'f' : 5 , 'g' : 1 , 'h' : 100}

unique_values = set(d.values())

print(f"Unique Values : {unique_values}")