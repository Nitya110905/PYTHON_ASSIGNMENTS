# Write a Python program to convert a list of characters into a 
# string.


l = ['a' , 'b' , 'c']


word = l[0]
for i in range(1,len(l)):
    word = word + l[i]

final_string = word

print("String formed is : ", final_string)


# or use "".join(l)