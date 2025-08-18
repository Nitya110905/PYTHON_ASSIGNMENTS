# Write a Python program to read an entire text file. 
# Write a Python program to append text to a file and display the 
# text. 


file = open("test.txt", "a")
file.write("Hello")
file.close()

file1 = open("test.txt", "r")
print(file1.read())
file1.close()