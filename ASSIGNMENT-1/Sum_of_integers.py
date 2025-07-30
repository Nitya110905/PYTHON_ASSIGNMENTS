# Write a Python program to sum of three given integers. 
# However, if two values are equal sum will be zero.

def sum_three_integers(a, b, c):
  if a == b or b == c or a == c:
    return 0
  else:
    return a + b + c

print(f"Sum of (1, 2, 3): {sum_three_integers(1, 2, 3)}")
print(f"Sum of (2, 2, 3): {sum_three_integers(2, 2, 3)}")
print(f"Sum of (5, 5, 5): {sum_three_integers(5, 5, 5)}")
print(f"Sum of (10, -5, 15): {sum_three_integers(10, -5, 15)}")