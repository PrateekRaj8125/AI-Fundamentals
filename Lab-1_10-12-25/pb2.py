# 2. Tuple Tasks

# I. Tuple Creation & Deletion
t = (10, 20, 30)
print(t)

del t   # Deletes entire tuple

# II. Tuple Duplication
t = (1, 2, 3)
dup = t * 3
print(dup)

# III. Tuple Length
t = (10, 20, 30)
print(len(t))

# IV. Accessing Tuples
# Positive Indexing
t = (10, 20, 30, 40)
print(t[0], t[2])

# Negative Indexing
print(t[-1], t[-3])

# Range (slice)
print(t[1:3])     # positive range
print(t[-3:-1])   # negative range

# Checking
print(20 in t)

# V. Tuple → List
t = (1, 2, 3)
l = list(t)
print(l)

# VI. Add & Remove Items in Tuple

# (Tuples are immutable → convert to list)

t = (1, 2, 3)
l = list(t)
l.append(4)
l.remove(2)
t = tuple(l)
print(t)

# VII. Looping through Tuples
    # for loop
t=(1,3,4)
for x in t:
    print(x)

    # while loop
i = 0
while i < len(t):
    print(t[i])
    i += 1

# VIII. Tuple Joining & Multiplication
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # join
print(t1 * 3)    # repeat

# IX. count() & index()
t = (1, 2, 2, 3, 4)
print(t.count(2))
print(t.index(3))