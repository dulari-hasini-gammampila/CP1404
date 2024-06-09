name = input("Name: ")
file = open("name.txt", "w")
print(name, file=file)
file.close()

file = open("name.txt", "r")
name = file.read().strip()
file.close()
print(f"Hello {name}")

with open("numbers.txt", "r") as file:
    number_one = int(file.readline().strip())
    number_two = int(file.readline().strip())
result = number_one + number_two
print(fresult)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)
