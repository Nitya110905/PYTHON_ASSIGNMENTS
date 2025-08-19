# Write a Python program to read a file line by line 
# store it into a variable.

file_path = 'sample_log.txt'

try:
    with open(file_path, 'r') as file:
        file_content_string = file.read()
    
    print("File content stored in a single string:")
    print(file_content_string)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")