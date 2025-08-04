# Write a Python function that takes a list of words and returns 
# the length of the longest one. 


def longest_word(list_words):
    max_length = 0
    longest_word = ""
    for word in list_words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word

    return longest_word, max_length


l = []

while True:
    inp = input("Enter word : ")
    l.append(inp)
    final_word , final_length = longest_word(l)
    print(f"Current words list: {l}")
    print(f"The longest word is: '{final_word}' with a length of {final_length}")
    out = input("Would You like to exit? Yes or No?").lower()
    if (out == "yes"):
        break