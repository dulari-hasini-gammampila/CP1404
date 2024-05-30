def main():
    score = float(input("Enter the score: "))
    score = get_valid_score(score)
    print("(G)et,\n(R)esult,\n(S)how\n(Q)uit")
    choice = input(">>> ")
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter the score: "))
            score = get_valid_score(score)
        elif choice == "R":
            result = get_result(score)
            print(result)
        elif choice == "S":
            stars = print_stars(score)
            print(stars)
        else:
            print("Invalid choice")

        print("(G)et,\n(R)esult,\n(S)how\n(Q)uit")
        choice = input(">>> ")
    print("Farewell")


def get_valid_score(score):
    """determine the score validation"""
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter the score: "))
    return score


def get_result(score):
    """determine the result based on score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """return starts"""
    return "*" * int(score)


main()
