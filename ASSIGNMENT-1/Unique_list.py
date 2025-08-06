# Write a Python program to remove duplicates from a list.

l = [1 , "abc" , 2 , 3 , 2 , 8 , 1 , "b" , "zzz" , "abc" , 2]
l1 = []


for item in l:
    if item not in l1:
        l1.append(item)
print("Unique List :" , l1)
    
# OR

original_list = [1, 2, 2, 3, 4, 4, 4, 5]

unique_set = set(original_list)

unique_list = list(unique_set)

print(unique_list)