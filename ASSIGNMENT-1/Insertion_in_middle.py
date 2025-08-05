# Write a Python function to insert a string in the middle of a string. 

def middle(original_string,string_to_insert):
    middle_index = len(original_string) // 2
    return original_string[:middle_index] + string_to_insert + original_string[middle_index:]

user_sentence = input("Enter Desired Sentence or Word :")
user_word = input("Enter word to be inserted in middle of sentence : ")

result = middle(user_sentence,user_word)

print(f"Your sentence : {user_sentence}")
print(f"Your word : {user_word}")
print(f"Final Result : {result}")