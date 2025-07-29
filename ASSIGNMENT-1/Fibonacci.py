term = int(input("Enter thr no. of terms you want in input : "))

n1 , n2 = 0 , 1

print("Fibonacci for ", term , "terms : ",n1,n2, end=" ")
for i in range(term-2):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 , n2 = n2 , n3