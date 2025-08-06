# Differentiate between append () and extend () methods? 
# -> append adds a singlr object at the end of the list while extend is used to end a block or multiple objects at the end of list.

l = [1 , 2 , 22 , 56 , 90]

l.append(89)

print(l)

l.extend(["hello",95,"@@@"])
print(l)