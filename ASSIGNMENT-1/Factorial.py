# Write a Python program to get the Factorial number of given 
# number.
n  = int(input("Enter the no. for its factorial :"))

def fact(n):
    if (n<0):
        return "Enter a positive integer"
    elif n == 0 or n ==1 :
        return n
    else :
        return n*fact(n-1)
    
result = print(fact(n))