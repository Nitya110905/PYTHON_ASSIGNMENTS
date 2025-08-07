# Write a Python function that takes two lists and returns true if 
# they have at least one common member.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 1, 10]

has_common = False
for item in list1:
    if item in list2:
        has_common = True

if has_common:
    print("The lists have at least one common element.")
else:
    print("The lists have no common elements.")
