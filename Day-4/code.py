# "for" Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using "range()" function
for i in range(1, 6):
    print(i)

# "while" Loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1


# ---- control loops "break", "continue", "else"
# 1. Use "break"
for num in range(1, 10):
    if num == 5:
        break
    print(num)

# 2. Use "continue"
for num in range(1, 6):
    if num == 3:
        continue
    print(num)  # Skips 3

# 2. Use "else"
for num in range(1, 5):
    print(num)
else:
    print("Loop finished")


# nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
