# Write a Python program to replace last value of tuples in a list. 

l = [(1 , 2 , 2) , (1 , 1 , 1) , (1 , 2 , 3)]

replacement_value = 100

updated_l = [t[:-1] + (replacement_value,) for t in l]

print(f"Original List : {l}" )
print(f"Updated List : {updated_l}")