# Write a Python program to check multiple keys exists in a 
# dictionary 


def check_keys_exist_all(my_dict, keys_to_check):
  return all(key in my_dict for key in keys_to_check)

person_data = {
    'name': 'Aarav',
    'age': 35,
    'city': 'Ahmedabad',
    'occupation': 'Engineer'
}

keys1 = {'name', 'city'}
if check_keys_exist_all(person_data, keys1):
  print(f"Success: All keys in {keys1} exist in the dictionary.")
else:
  print(f"Failure: Not all keys in {keys1} exist in the dictionary.") 

keys2 = ['name', 'salary'] # Using a list also works
if check_keys_exist_all(person_data, keys2):
  print(f"Success: All keys in {keys2} exist in the dictionary.")
else:
  print(f"Failure: Not all keys in {keys2} exist in the dictionary.")