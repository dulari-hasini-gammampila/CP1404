def main(password=None):
    password = get_password(password)
    while len(password) < 8:
        print("Password is doesnt have meet minimum length")
        password = get_password(password)

    print("*" * len(password))


def get_password(password):
    password = input("Enter password: ")
    return password


main()
