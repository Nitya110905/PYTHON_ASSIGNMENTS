# Write a Python program to add 'ing' at the end of a given 
# string (length should be at least 3). If the given string already 
# ends with 'ing' then add 'ly' instead if the string length of the 
# given string is less than 3, leave it unchanged. 

def add_ing(word):
    length = int(len(word))

    if length < 3:
        final_word = word

    elif word.endswith("ing"):
        final_word = word + "ly"
    else:
        final_word = word + "ing"
        
    return final_word



word = input("Enter Your desired String : ")
resulting_word = add_ing(word)
print(f"Your final word is {resulting_word}")




# slice_word = word[(length-3):length:1]
    # print(slice_word)
    # if slice_word == "ing":