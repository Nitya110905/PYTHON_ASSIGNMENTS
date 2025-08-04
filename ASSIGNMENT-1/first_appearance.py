def remove_not_poor(sentence):
    snot = sentence.find("not")
    spoor = sentence.find("poor")

    if snot < spoor:
       sentence = sentence.replace(sentence[snot:spoor + 4],"good")
    
    return sentence


user_input = input("Enter a sentence : ")
final_sentence = remove_not_poor(user_input)

print(f"Your final sentence is '{final_sentence}'")