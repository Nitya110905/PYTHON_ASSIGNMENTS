# Write a Python function that checks whether a passed string is 
# palindrome or not


user = input("Enter a String :")
user = user.lower()
palindrome = user[::-1]

if user == palindrome:
    print(f"{user} is palindrome")
else:
    print(f"{user} is not palindrome")