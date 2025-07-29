n  = int(input("Enter the no. for its factorial :"))

def fact(n):
    if n == 0 or n ==1 :
        return n
    else :
        return n*fact(n-1)
    
result = print(fact(n))