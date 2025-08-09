# Write a Python program to find the second smallest 
# number in a list.


def find_second_smallest(numbers):
    unique_nums = list(set(numbers))

    unique_nums.sort()

    if len(unique_nums) < 2:
        return None  
    else:
        
        return unique_nums[1]

# --- Sample Usage ---
my_list1 = [1, 10, 5, 2, 8, 1, 9, 2]
my_list2 = [5, 5, 5]  
my_list3 = []         

second_smallest1 = find_second_smallest(my_list1)
second_smallest2 = find_second_smallest(my_list2)
second_smallest3 = find_second_smallest(my_list3)

print(f"Original List: {my_list1}")
print(f"Second Smallest Number: {second_smallest1}")
print(f"Original List: {my_list2}")
print(f"Second Smallest Number: {second_smallest2}")
print(f"Original List: {my_list3}")
print(f"Second Smallest Number: {second_smallest3}")