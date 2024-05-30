
for i in range(0, 101, + 10):
    print(i, end=" ")

# b)

for i in range(20, 0, -1):
    print(i, end=" ")

# c)

number = int(input("Number: "))
for i in range(number):
    print("*", end=" ")

# d

number = int(input("Number: "))
for i in range(1, number + 1):
    print("*" * i)
