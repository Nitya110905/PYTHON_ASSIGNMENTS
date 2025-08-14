# Write a Python program to returns sum of all divisors of a 
# number


user = int(input("Enter a number : "))

div = []
for i in range(1,user+1):
    if user % i == 0:
        div.append(i)
print(sum(div))