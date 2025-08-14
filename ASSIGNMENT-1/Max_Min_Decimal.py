# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.


numbers = input("Enter decimal numbers separated by spaces: ")

decimal_list = [float(num) for num in numbers.split()] # split() in Python is a string method that breaks a string into a list, based on a separator you give it.

# Finding max and min
maximum = max(decimal_list)
minimum = min(decimal_list)

print(f"Maximum number: {maximum}")
print(f"Minimum number: {minimum}")
