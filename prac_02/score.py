import random


def main():
    """print user input score result and random score result"""
    score = float(input("Enter score: "))
    print(get_result(score))
    random_score = random.randint(0, 100)
    print(get_result(random_score))


def get_result(score):
    """determine the result based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()
