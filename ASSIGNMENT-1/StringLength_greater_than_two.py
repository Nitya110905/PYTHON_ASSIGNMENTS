# Write a Python program to count the number of strings where 
# the string length is 2 or more and the first and last character 
# are same from a given list of strings.


l = ["abc" , "wewe" , "a" , "zzz" , "bvdiugchsib"]
count = 0
for word in l:
    # if len(word) >= 2 and word[0:1] == word[(len(word) - 1) : len(word)]:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
        print("Word : ",word)

print("Total Count : ",count)