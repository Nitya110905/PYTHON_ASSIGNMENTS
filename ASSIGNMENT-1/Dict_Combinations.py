# Write a Python program to create and display all combinations 
# of letters, selecting each letter from a different key in a 
# dictionary. 
# o Sample data: {'1': ['a','b'], '2': ['c','d']} o Expected Output: 
# o ac ad bc bd 


import itertools

data = {'1': ['a', 'b'], '2': ['c', 'd']}

value_lists = data.values()

# Use itertools.product to get all combinations
# The * operator unpacks the list of lists into separate arguments for product()
combinations = itertools.product(*value_lists)

# Iterate through the combinations and join them into strings
for combo in combinations:
    print(''.join(combo), end=' ')





# d = {'1': ['a','b'], '2': ['c','d']}

# l = d.get('1')
# l1 = d.get('2')

# for value in l:
#     for value1 in l1:
#         res = value+value1
#         print (res)

