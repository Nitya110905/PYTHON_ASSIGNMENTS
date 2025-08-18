# Write a Python program to read last n lines of a file.

from collections import deque

def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            # Create a deque with a maximum length of n
            last_lines = deque(file, maxlen=n)
        
        print(f"--- Last {n} lines of {file_path} ---")
        for line in last_lines:
            print(line.rstrip())
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")



# 2. Now, call the function to read the last 3 lines of the file
read_last_n_lines("sample_log.txt", 3)