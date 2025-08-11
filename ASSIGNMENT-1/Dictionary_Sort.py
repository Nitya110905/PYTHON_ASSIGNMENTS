# Write a Python script to sort (ascending and descending) a 
# dictionary by value.

import operator

d = {'a': 1, 'b': 2, 'c': 7, 'd': 5, 'e': 4}

# --- Ascending Sort ---

sorted_asc = dict(sorted(d.items(), key=lambda item: item[1]))

print("Ascending sort by value:")
print(sorted_asc)


# --- Descending Sort ---

sorted_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("\nDescending sort by value:")
print(sorted_desc)