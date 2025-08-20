# Write a Python program to count the frequency of words in a file.



import string
def frequency(file_name):
    f = {}
    translator = str.maketrans('','',string.punctuation)
    with open(file_name,"r") as file:
        for line in file:
            words = line.split()

            for word in words:
                cleaned_word = word.lower()
                cleaned_word = cleaned_word.translate(translator)
                f[cleaned_word] = f.get(cleaned_word,0) + 1
            
        return f
    
final_frequency = frequency("sample_log.txt")

for key,count in final_frequency.items():
    print(f"{key} : {count}")
    
            

