# Write a python program to find the longest words.


import string

def find_longest_word_in_file(file_path):
    longest_word = ""
    with open(file_path,"r") as file:
        for lines in file:
            words = lines.split()

            for word in words:
                translator = str.maketrans('','',string.punctuation)
                cleaned_word = word.translate(translator)


                if len(cleaned_word) > len(longest_word):
                    longest_word = cleaned_word

    return longest_word

file_path = 'sample_log.txt' 
# Assuming you have a file named my_document.txt
# with content like: "Python is a powerful programming language."

result = find_longest_word_in_file(file_path)
print(f"The longest word in the file is: '{result}'")