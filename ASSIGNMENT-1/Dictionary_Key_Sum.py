# Write a Python program to combine two dictionary adding 
# values for common keys. 
# o d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 
# 200,’d’:400} 
# • Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).


d1 = d = {'a': 100, 'b': 200, 'c': 300}

d2 = {'a': 300, 'b': 200 , 'd': 400}
new_d = d1 | d2

for key in d1:
    for key1 in d2:
        if key == key1:
            new_d [key] = (d1.get(key) + d2.get(key1))

print(new_d)


# A better Way!
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}

# new_d = d1.copy()

# for key, value in d2.items():
#     new_d[key] = new_d.get(key, 0) + value

# print(new_d)
