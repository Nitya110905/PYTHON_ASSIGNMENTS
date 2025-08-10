# Write a Python program to unzip a list of tuples into individual 
# lists. 

l = [(1 , 2 , 2) , () , (1 , 1 , 1) , () , (1 , 2 , 3)]

for item in l:
    l1 = list(item)
    print(l1)