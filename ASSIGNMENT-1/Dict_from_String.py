#     Write a Python program to create a 
# dictionary from a string. 
# o Note: Track the count of the letters from the 
# string. Sample string: 
# 'w3resource' 
# o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 
# 2, 'o': 1} 

from collections import Counter

word = "w3resource"

d = Counter(word)

print(d)