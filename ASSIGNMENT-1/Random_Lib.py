import random

# How can you pick a random item from a range? 
random_even = random.randrange(10, 20, 2)
print(random_even) 

# How can you get a random number in python? 
print(random.randint(1,100))

# How will you set the starting value in generating random 
# numbers?
print(f"A random float: {random.random()}")

random_price = random.uniform(50.50, 99.99)
print(f"Your random price is: {random_price:.2f}")

# How will you randomizes the items of a list in place? 
random.seed(42)
print(random.randint(1, 100)) # These specific numbers aren't magical. They are simply the deterministic output of the Mersenne Twister algorithm when given the initial state (seed) of 42.
print(random.randint(1, 100))

# Write a Python program to read a random line from a file. 
def get_random_line(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            random_line = random.choice(lines)
            
            return random_line.strip()
    except FileNotFoundError:
        return "Error: The file was not found."
    except IndexError:
        return "Error: The file is empty."

file_name = "quotes.txt"
random_quote = get_random_line(file_name)

print("Here is your random quote of the day:")
print(random_quote)