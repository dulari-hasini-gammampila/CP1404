"""
start date = 2024 july 15
start time = 1.50PM
"""

FILENAME = "projects.txt"
menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    # print(f"Loaded {} projects from {FILENAME}")
    print("Welcome to Pythonic Project Management")
    choice = False
    while choice != "Q":
        print(menu)
        choice = input(">>> ").upper()
        if choice == "L":
            project = load_projects(FILENAME)
        # elif choice == "S":
        #     save = save_projects(FILENAME)
        # elif choice == "D":
        #     project_list = display_projects(projects)
        # elif choice == "F":
        #     filter_projects = filter_projects_by_date(projects)
        # elif choice == "A":
        #     new_projects = add_new_projects(projects)
        # elif choice == "U":
        #     modify_projects = update_projects(projects)
        # elif choice == "Q":
        #     user_choice = input("Would you like to save to projects.txt? ").upper()
        #     while user_choice != "NO":
        #         if user_choice == "YES":
        #             save = save_projects(FILENAME)
        #             print("Thank you for using custom-built project management software.")
        #         elif choice == "NO":
        #             print("Thank you for using custom-built project management software.")
        #         else:
        #             print("Please yes or no")
        #             user_choice = input("Would you like to save to projects.txt? ").upper()
        # else:
        #     print("You have entered invalid menu option")

def load_projects(FILENAME):
    projects = []

    with open(FILENAME, "r") as infile:
        for readline in infile:
            projects.append(readline)
            print(readline)
































main()
