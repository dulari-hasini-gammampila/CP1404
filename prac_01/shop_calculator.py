total = 0

number_of_items = int(input("Number of items: "))
while number_of_items <= 0:  # until enter valid item number
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total += item_price

if total > 100:
    discount = total * 10 / 100
    total -= discount

print(f"Total price for {number_of_items} is ${total:.2f}")