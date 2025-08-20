# How Do You Handle Exceptions With Try/Except/Finally In 
# Python? Explain with coding snippets.

try:
    n = int(input("Enter no. "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError as e:
    print(e)
else :
    print("Try Executed!!!")
finally:
    print("Finally Executed!")

