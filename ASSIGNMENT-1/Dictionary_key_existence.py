# Write a Python script to check if a given key already 
# exists in a dictionary.

d = {'a': 1, 'b': 2, 'c': 7, 'd': 5, 'e': 4}

user_key = input("Enter a key: ")

if user_key in d:
    print(f"The key '{user_key}' exists in the dictionary.")
else:
    print(f"The key '{user_key}' does not exist in the dictionary.")