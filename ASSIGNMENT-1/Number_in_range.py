# Write a Python function to check whether a number is in a given 
# range 

def is_in_range(number_to_check, range_start, range_end):
  
  return range_start <= number_to_check <= range_end


start_of_range = 1
end_of_range = 100
try:
  user_number = int(input(f"Enter a number to check if it's between {start_of_range} and {end_of_range}: "))

  if is_in_range(user_number, start_of_range, end_of_range):
    print(f"Yes, {user_number} is in the range.")
  else:
    print(f"No, {user_number} is not in the range.")
except ValueError:
  print("Invalid input. Please enter a whole number.")