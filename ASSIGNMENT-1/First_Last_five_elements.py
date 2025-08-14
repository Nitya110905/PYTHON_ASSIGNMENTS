# Write a Python program to generate and print a list of first 
# and last 5 elements where the values are square of 
# numbers between 1 and 30. 

l = [ 1 , 9 , 4 , 25 , 88 , 33 , 49 , 900 , 625 , 89 , 121 , 576 , 99 , 0 ]

# raise the variable i to the power of 2
all_squares = [i**2 for i in range(1, 31)]

first_5_elements = all_squares[:5]

last_5_elements = all_squares[-5:]

print("First 5 elements:", first_5_elements)
print("Last 5 elements:", last_5_elements)