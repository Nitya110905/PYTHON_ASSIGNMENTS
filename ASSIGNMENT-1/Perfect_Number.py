# Write a Python function to check whether a number is 
# perfect or not.


import math

def is_perfect(number):
  if not isinstance(number, int) or number <= 1:
    return False
  sum_of_divisors = 1
  
  for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
      sum_of_divisors += i
      pair = number // i
      if pair != i:
        sum_of_divisors += pair
        
  return sum_of_divisors == number

print(f"Is 6 a perfect number?   -> {is_perfect(6)}")
print(f"Is 28 a perfect number?  -> {is_perfect(28)}")
print(f"Is 496 a perfect number? -> {is_perfect(496)}")
print(f"Is 10 a perfect number?  -> {is_perfect(10)}")
print(f"Is 1 a perfect number?   -> {is_perfect(1)}")