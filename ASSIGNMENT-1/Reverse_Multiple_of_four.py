# Write a Python function to reverses a string if its length is a 
# multiple of 4.

def reverse_string(word):

    if len(word) % 4 == 0:
       return word[::-1]
    return word

user = input("Enter a String : ")

final_word = reverse_string(user)

print(f"Your final word is : {final_word}")




