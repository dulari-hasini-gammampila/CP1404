
def main():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("celsius: "))
            result = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {result:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            result = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {result:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """covert fahrenheit using celsius """
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """convert celsius using fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
