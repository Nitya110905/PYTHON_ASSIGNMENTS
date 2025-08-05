# Write a Python program to get a string made of the first 2 
# and the last 2 chars from a given a string. If the string length 
# is less than 2, return instead of the empty string. 
# o Sample String: w3resource' o 
# Expected Result: 'w3ce' o 
# Sample String: 'w3'   o Expected 
# Result: 
# 'w3w3'   o Sample String: ' w' o 
# Expected Result: Empty String 

def result_word(word):
    length = len(word)
    if length < 2:
        print("Empty String!!!")
    else:
        first_two = word[0:2]
        last_two = word[(length-2) : length ]

        final_res = first_two + last_two

        print(f"Your first two characters are '{first_two}' & last two characters are '{last_two}'")
        print(f"Final word formed is : {final_res}")


user = input("Enter a word : ")
result_word(user)