password = input("Enter Password: ")
while len(password) < 8:
    print("Password is doesnt have meet minimum length")
    password = input("Enter Password: ")

print("*" * len(password))
