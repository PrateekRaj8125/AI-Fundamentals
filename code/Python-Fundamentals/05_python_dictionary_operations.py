# Implement dictionary operations including creation, updating, deletion, looping, and nested dictionaries.
# I. Dictionary Creation + Access + Update
d = {"name": "John", "age": 25}
print(d["name"])

d["age"] = 30
d["city"] = "Delhi"
print(d)

#II. Length, Type, dict() Constructor
print(len(d))
print(type(d))

d2 = dict(name="Amit", age=22)
print(d2)

#III. Add & Remove Items
d["country"] = "India"

d.pop("age")
d.popitem()   # removes last item
print(d)

#IV. clear() and del
d.clear()
del d

#V. Looping & Copying Dictionary
d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(key, d[key])

copy_d = d.copy()
print(copy_d)

#VI. Nested Dictionary
students = {
    "s1": {"name": "John", "age": 20},
    "s2": {"name": "Amit", "age": 22}
}

print(students["s1"]["name"])

for sid, info in students.items():
    print(sid, info)