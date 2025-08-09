# Write a Python program to select an item randomly from a list.

import random

programming_languages = ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Rust', 'Swift']

random_language = random.choice(programming_languages)

print(f"Original list: {programming_languages}")
print(f"Randomly selected item: {random_language}")