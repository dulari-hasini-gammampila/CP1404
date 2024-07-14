from guitar import Guitar
from operator import attrgetter


def main():
    """Get user ingut for guitar name, year, cost and append these information into a list"""
    guitars = []

    print("My guitars!")
    name = input("Name: ").strip()
    max_name_length = len(name) if name else 0
    max_cost_length = 0
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        max_name_length = max(max_name_length, len(name)) # keep max length of name for spacing
        max_cost_length = max(max_cost_length, len(f"{cost:,.2f}")) #keep max length of cost for cost spacing
        name = input("Name: ").strip()
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))  #for testing
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # max_name_length = max(len(guitar.name) for guitar in guitars)
    # max_cost_length = max(len(f"${guitar.cost:,.2f}") for guitar in guitars)
    if not guitars:
        print("No guitars entered.")
    else:
        guitars.sort(key=attrgetter('year')) # Sort guitars by year using attrgetter
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
            guitar_name = f"{guitar.name:<{max_name_length}}"
            guitar_cost = f"{guitar.cost:,.2f}"
            print(f"Guitar {i}: {guitar_name} ({guitar.year}), worth $ {guitar_cost:>{max_cost_length}}{vintage_string}")


main()
