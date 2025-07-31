# Write a Python program to count the number of characters 
# /character frequency/ in a string

def count_char(str):
    frequency = {}

    for char in str :
        frequency[char] = frequency.get(char,0) + 1
    return frequency
# It tries to get the value associated with the char (the current character) from the frequency dictionary.
# If char is already a key in the frequency dictionary (meaning we've encountered this character before), it returns its current count.
# If char is not yet a key in the frequency dictionary (meaning this is the first time we're seeing this character), get() returns the default value specified, which is 0 in this case.

str = input("Enter a string :")
res = count_char(str)

# Now res is a dictionary

for char, count in res.items():
    print(f"'{char}': {count}")
