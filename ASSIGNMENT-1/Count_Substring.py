# Write a Python program to count occurrences of a substring in a 
# string. 


def count_substring(orig_string,sub_string):
    count = 0
    start_index = 0
    while True:
        start_index = orig_string.find(sub_string,start_index )

        if start_index == -1:
            break

        count += 1
        start_index += 1

    return count




orig_string = "Hello World! Hello!!"
    
sub_string = input("Kindly Enter a String")

count = count_substring(orig_string, sub_string)
if count == 1:
    print(f"For {orig_string}, the occurence of {sub_string} is {count} time")
else:
        print(f"For {orig_string}, the occurence of {sub_string} is {count} times")