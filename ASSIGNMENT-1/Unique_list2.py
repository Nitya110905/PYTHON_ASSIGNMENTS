# Write a Python function that takes a list and returns a new list 
# with unique elements of the first list. 

def unique_list(list1):
    new_list = []
    for n in list1:
        if n not in new_list:
            new_list.append(n)
    return new_list

l1 = []

while True:
    n = input("Type e to exit ! Enter elements for your list : ")
    if n == "e":
        break
    l1.append(n)

final_list = unique_list(l1)
print("Final List :", final_list)