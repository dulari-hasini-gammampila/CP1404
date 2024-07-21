"""
start date = 2024 july 15
start time = 1.50PM

"""

from project import Project
from operator import itemgetter

FILENAME = "projects.txt"
menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print("Welcome to Pythonic Project Management")
    choice = False
    while choice != 'q':
        print(menu)
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(FILENAME)
            print(f"Loaded {len(projects)} projects from {FILENAME}")
        elif choice == 's':
            save_choice = input(f"Would you like to save to {FILENAME}? ").strip().lower()
            if save_choice.startswith('y'):
                save_project = save_projects(projects, FILENAME)
                print(f"Projects saved to {FILENAME}")
        elif choice == 'd':
            show_project = display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            sorted_projects = filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            updated_projects = update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {FILENAME}? ").strip().lower()
            if save_choice.startswith('y'):
                save_project = save_projects(projects, FILENAME)
                print(f"Projects saved to {FILENAME}")
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice. Please try again.")


def load_projects(FILENAME):
    """Load projects from a file."""
    projects = []

    with open(FILENAME, 'r') as infile:
        next(infile)
        for line in infile:
            if line.strip():
                parts = line.strip().split()
                projects.append(Project(parts))
    return projects


def save_projects(projects, FILENAME):
    """"""


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate ($): ")
    completion_percentage = input("Percent complete: ")


def update_project(projects):
    """Update completion percentage and priority of a project."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    if not projects:
        print("No projects to update.")
        return
    try:
        index = int(input("Project choice: "))
        if 0 <= index < len(projects):
            new_completion = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_completion:
                projects[index].completion_percentage = int(new_completion)
            if new_priority:
                projects[index].priority = int(new_priority)
            print("Project updated successfully.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def display_projects(project):
    """Display formatted data of projects by name, start date, priority, cost estimate, completion percentage, and calculate incomplete projects."""
    incomplete_count = 0
    total_cost_estimate = 0.0
    number = 0
    formatted_projects = []

    max_name_length = max(len(project.name.strip()) for project in projects)
    max_start_date_length = max(len(project.start_date.strftime('%d/%m/%Y')) for project in projects)
    max_priority_length = max(len(str(project.priority)) for project in projects)
    max_cost_estimate_length = max(len(f"${project.cost_estimate:.2f}") for project in projects)
    max_completion_length = max(len(str(project.completion_percentage)) for project in projects)
    projects.sort(key=itemgetter('priority', 'name'))
    for project in projects:
        number += 1
        if project['completion_percentage'] < 100:
            incomplete_count += 1
            total_cost_estimate += project['cost_estimate']
            formatted_projects.append(
                f"*{number}. {project['name']:<{max_name_length}} | {project['start_date'].strftime('%d/%m/%Y'):<{max_start_date_length}} | {project['priority']:<{max_priority_length}} | ${project['cost_estimate']:.2f} | {project['completion_percentage']}%"
            )
        else:
            formatted_projects.append(
                f" {number}. {project['name']:<{max_name_length}} | {project['start_date'].strftime('%d/%m/%Y'):<{max_start_date_length}} | {project['priority']:<{max_priority_length}} | ${project['cost_estimate']:.2f} | {project['completion_percentage']}%"
            )
    for project in formatted_projects:
        print(project)
    print_project_status(incomplete_count, total_cost_estimate)


def print_project_status(incomplete_count, total_cost_estimate):
    """Print message based on number of incomplete projects and total cost estimate."""
    if incomplete_count > 0:
        print(
            f"There are {incomplete_count} incomplete projects with a total cost estimate of ${total_cost_estimate:.2f}.")
    else:
        print("All projects are completed. Great job!")


def filter_projects_by_date(projects, date):
    """Filter projects that start after the given date."""
    filtered_projects = [project for project in projects if
                         project['start_date'] > datetime.datetime.strptime(date, "%d/%m/%Y").date()]
    return filtered_projects


main()
