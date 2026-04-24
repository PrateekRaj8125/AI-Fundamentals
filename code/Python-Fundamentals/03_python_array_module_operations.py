# Implement array operations using Python’s array module including traversal, insertion, and deletion.
    #from array import array

#I. Array Creation
from array import array
a = array('i', [10, 20, 30])
print(a)

#II. Array Element Access
print(a[0], a[2])

#III. Array Length
print(len(a))

#IV. Looping Array Elements
for x in a:
    print(x)

#V. append()
a.append(40)
print(a)
a.pop()

#VI. pop()
a.pop()
print(a)