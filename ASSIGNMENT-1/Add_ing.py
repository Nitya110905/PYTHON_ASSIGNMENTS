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