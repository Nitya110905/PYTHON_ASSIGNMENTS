# Write a Python program to count the number of lines in a text 
# file. 

count = 0
file_name = "sample_log.txt"
with open(file_name,"r") as file:
    for lines in file:
        count += 1
    print(f"There are a total of {count} no. of lines in {file_name} ")