# Write a Python program to count the occurrences of each word 
# in a given sentence


# str.maketrans(x, y, z)

# x (first argument): A string specifying characters to be replaced.

# y (second argument): A string specifying the characters to replace them with. x and y must have the same length.

# z (third argument): A string specifying characters to be deleted.


import string

def count_Words(sentence):
    d = {}
    lower_case = sentence.lower()
    translator = str.maketrans('','',string.punctuation)    
    lower_case = lower_case.translate(translator)

    seperate_words = lower_case.split()

    for word in seperate_words:
        d[word] = d.get(word,0) + 1
    
    return d


sentence = "Hello ! Hello ! How are You ? Hello ? You There ?"

counts = count_Words(sentence)
for word,count in counts.items():
    print(f"{word} : {count}")