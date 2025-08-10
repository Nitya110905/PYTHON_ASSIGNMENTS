# Write a Python program to find the repeated items of a tuple. 

# Sample tuple with repeated items
my_tuple = ('a', 'b', 'c', 'b', 'd', 'm', 'n', 'n')

print(f"Original Tuple: {my_tuple}")

seen = set()
duplicates = set()

for item in my_tuple:
  if item in seen:
    duplicates.add(item)
  else:
    seen.add(item)

print(f"Repeated Items: {list(duplicates)}")