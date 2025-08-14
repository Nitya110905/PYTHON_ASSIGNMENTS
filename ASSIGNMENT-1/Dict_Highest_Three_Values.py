# Write a Python program to find the highest 3 values in a 
# dictionary


d = {'a' : 10 , 'b' : 2 , 'c' : 102 , 'd' : 555 , 'e' : 100 , 'f' : 500 , 'g' : 1 , 'h' : 109}

l = list(d.values())

l.sort()

print(l[-3]," ",l[-2]," ",l[-1])

# Using heapq
# import heapq

# d = {'a' : 10 , 'b' : 2 , 'c' : 102 , 'd' : 555 , 'e' : 100 , 'f' : 500 , 'g' : 1 , 'h' : 109}

# highest_3 = heapq.nlargest(3, d.values())

# print(highest_3)