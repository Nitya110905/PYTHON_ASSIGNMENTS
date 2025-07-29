# Write a Python program to find whether a given number is 
# even or odd, print out an appropriate message to the user.


n = int(input("Enter a no."))

if n%2 == 0:
    print(f"{n} is even!")
else:
    print(f"{n} is odd!")