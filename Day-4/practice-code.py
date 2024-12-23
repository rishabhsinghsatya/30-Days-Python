# 1. Sum of First N Numbers
n = int(input("Enter a number:"))
total = 0
for i in range(1, n + 1):
    total += i
print("sum:", total)


# 2. Multiplication Table
n = int(input("Enter a number:"))
for i in range(1, 11):
    print(f"{n}*{i} = {n*i}")


# 3. Guessing Game
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Enter ur guess number:"))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too higher")
print("Congratulation! U guessed it")


# 4. Pattern Printing
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)
