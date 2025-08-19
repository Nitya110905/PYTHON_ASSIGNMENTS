# Write a Python program to read a file line by line and store it 
# into a list

l = []

with open("sample_log.txt","r") as file:
    l = [line.rstrip() for line in file]

print(l)