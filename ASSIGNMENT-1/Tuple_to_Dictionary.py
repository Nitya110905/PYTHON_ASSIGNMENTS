# Write a Python program to convert a list of tuples into a 
# dictionary.  

l = [(1 , 2 , 2) , () , (1 , 1 , 1) , () , (1 , 2 , 3)]
i = 0
d={}
for item in l:
    d[i] =  item
    i += 1
print(d)