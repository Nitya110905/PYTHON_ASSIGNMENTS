# Write a Python program that will return true if the 
# two given integervalues are equal or their sum or 
# difference is 5.

def two_integers(a,b):
    if a ==  b or a - b == 5 or a + b == 5 :
        return True
    else:
        return False
    

print(f"Output for (3,3) is : ",two_integers(3,3))
print(f"Output for (3,2) is : ",two_integers(3,2))
print(f"Output for (5,0) is : ",two_integers(5,0))
print(f"Output for (10,12) is : ",two_integers(10,12))