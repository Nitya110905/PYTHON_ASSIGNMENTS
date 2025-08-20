# Write python program that user to enter only odd numbers, 
# else will raise an exception. 


try:
    user = int(input("Enter a Number : "))
    if user % 2 == 0:
        raise ValueError("Number entered must be odd!!!")
    print(user)
except ValueError as e:
    print(e)
    