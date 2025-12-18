# 1. Conditional Statements + Loops
    # 1.1 if, if…else, elif
x = 15

# if
if x > 10:
    print(x, " is greater than 10")

# if...else
if x % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# if...elif...else
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")

# 1.2 Loops (for, while)
    # For Loop
for i in range(5):
    print("For loop:", i)

    # While Loop
count = 1
while count <= 5:
    print("While loop:", count)
    count += 1