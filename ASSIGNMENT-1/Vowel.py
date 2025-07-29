# Write a Python program to test whether a passed letter is a 
# vowel or not. 

letter = input("Enter a letter : ")
letter = letter.lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(f"{letter} is a vowel!")
else:
    print(f"{letter} is a consonant!")
