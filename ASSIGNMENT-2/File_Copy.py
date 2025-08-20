# Write a Python program to copy the contents of a file to another 
# file.

def copy(file_name):
    with open(file_name,"r") as file, open("test2.txt","w") as file1:
        for line in file:
            file1.write(line)

        
copy("sample_log.txt")