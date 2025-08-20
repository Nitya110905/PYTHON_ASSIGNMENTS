# Write a Python program to write a list to a file.

l = []


with open("test1.txt","w") as file:
    for i in range (1,31):
        l.append(i)
    file.write(str(l))