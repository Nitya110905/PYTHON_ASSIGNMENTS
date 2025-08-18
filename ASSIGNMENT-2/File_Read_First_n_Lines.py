# Write a Python program to read first n lines of a file.

def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file: # When you use with open(...), you are telling Python to manage the file's resources for you. It automatically handles closing the file as soon as the indented block of code under it is finished, even if an error occurs within that block
            print(f"--- First {n} lines of {file_path} ---")
            for i, line in enumerate(file):
                if i >= n:
                    break
                # print() adds a newline, so use rstrip() to remove the
                # newline character from the line read from the file.
                print(line.rstrip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")



with open("sample_log.txt", "w") as f:
    f.write("Line 1: System startup.\n")
    f.write("Line 2: Checking connections.\n")
    f.write("Line 3: Network OK.\n")
    f.write("Line 4: Loading user profiles.\n")
    f.write("Line 5: User 'admin' logged in.\n")
    f.write("Line 6: All services running.\n")

read_first_n_lines("sample_log.txt", 4)