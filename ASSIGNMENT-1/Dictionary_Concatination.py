# Write a Python script to concatenate following dictionaries to 
# create a new one. 


dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}
dic3 = {'e': 5, 'f': 6}

new_dict_unpack = {**dic1, **dic2, **dic3}

print("Concatenated using unpacking (**):")
print(new_dict_unpack)


new_dict_union = dic1 | dic2 | dic3

print("\nConcatenated using the union operator (|):")
print(new_dict_union)