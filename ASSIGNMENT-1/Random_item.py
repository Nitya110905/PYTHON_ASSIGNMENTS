# How can you pick a random item from a list or tuple?

import random


l = [1 , 2 , 3]
t = (1 , 2 , 3)

select = random.choice(l)
select1 = random.choice(t)

print(select," ", select1)