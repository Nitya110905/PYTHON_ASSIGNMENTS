# Write a python program to sum of the first n positive integers. 

def sum_of_n(n):

    if n<0 :
        return "Kindly enter a positive value"

    sum = 0

    for i in range(1,n+1):
        sum += i
    
    return sum

print(f"Sum of first 5 +ve integers : {sum_of_n(5)}")
print(f"Sum of first 10 +ve integers : {sum_of_n(10)}")
print(f"Sum of first 20 +ve integers : {sum_of_n(20)}")
print(f"Sum of first 50 +ve integers : {sum_of_n(50)}")

