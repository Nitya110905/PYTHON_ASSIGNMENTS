# Write a Python program to check whether an element 
# exists within a tuple. 

t = (1 , 2 , 3 , "abc" , "zzz")

exist = 1

if exist in t:
    print(f"Yes {exist} exists in tuple {t}")
else:
    print(f"No {exist}  doesn't exist in tuple {t}")

print(len(t))