# Write python program that swap two number with temp 
# variable and without temp variable.


# with temp
a , b = 1 , 2

print("Before Swapping a = ",a, " & b = ",b)

temp = a
a = b
b = temp

print("After Swapping a = ",a, " & b = ",b)


# without temp
a , b = 10 , 20

print("Before Swapping a = ",a, " & b = ",b)

a , b = b , a

print("After Swapping a = ",a, " & b = ",b)

