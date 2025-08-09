# Write a Python program to check whether a list contains a sub 
# list

def contains_sublist(main_list, sub_list):

    if not sub_list:
        return True

    if len(sub_list) > len(main_list):
        return False

    n = len(sub_list)
    return any(sub_list == main_list[i:i+n] for i in range(len(main_list) - n + 1))


list1 = [1, 2, 3, 4, 5, 6, 7]
sublist1_present = [3, 4, 5]
sublist2_absent = [3, 5, 6]
sublist3_empty = []

print(f"List: {list1}")
print(f"Sublist: {sublist1_present}")
print(f"Contains sublist? -> {contains_sublist(list1, sublist1_present)}")

print(f"List: {list1}")
print(f"Sublist: {sublist2_absent}")
print(f"Contains sublist? -> {contains_sublist(list1, sublist2_absent)}")

print(f"List: {list1}")
print(f"Sublist: {sublist3_empty}")
print(f"Contains sublist? -> {contains_sublist(list1, sublist3_empty)}")