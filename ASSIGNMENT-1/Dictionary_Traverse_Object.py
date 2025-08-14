# How Do You Traverse Through A Dictionary Object In Python?


capitals = {'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}

for country in capitals:
    city = capitals[country]
    print(f"The capital of {country} is {city}.")