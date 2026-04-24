# Perform set operations including union, intersection, difference, and symmetric difference.

#I. Set Creation & Length
s = {1, 2, 3}
print(len(s))

#II. Different Data Types
s = {1, "hello", 3.14, True}
print(s)

#III. Using set() Constructor
s = set([10, 20, 30])
print(s)

#IV. Accessing Set Items
for x in s:
    print(x)

#V. Add items (add, update)
s.add(40)
s.update([50, 60])
print(s)

#VI. remove(), pop(), discard()
s.remove(20)
s.discard(60)  # no error
s.pop()
print(s)

#VII. clear() & del
s.clear()
del s

#VIII. Looping (for, while)
s = {1, 2, 3}
for x in s:
    print(x)

s_list = list(s)
i = 0
while i < len(s_list):
    print(s_list[i])
    i += 1

#IX. Set Joining
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
a.update(b)
print(a)

print(a.intersection(b))
a.intersection_update(b)
print(a)

#X. More Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a.difference(b))
a.difference_update(b)
print(a)

print(a.isdisjoint(b))

print(a.symmetric_difference(b))