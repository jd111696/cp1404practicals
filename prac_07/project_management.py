""" CP1404 - Project Management

Estimated time: 60 minutes
Actual time:     minutes
"""

from project import Project
import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Python Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using this program!")


def load_projects(filename):
    """Load projects from a file, keeping dates as strings."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date_string = parts[1]
            start_date = parse_date(start_date_string)
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            date_string = project.start_date.strftime("%d/%m/%Y")
            print(f"{project.name}\t{date_string}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def add_new_project(projects):
    """Ask the user for project details and add the new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = parse_date(start_date_string)
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    """Choose a project and update its completion percentage and/or priority."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_choice = int(input("Project choice: "))
    chosen_project = projects[project_choice]
    print(chosen_project)

    new_percentage_input = input("New Percentage: ")
    if new_percentage_input != "":
        chosen_project.completion_percentage = int(new_percentage_input)

    new_priority_input = input("New Priority: ")
    if new_priority_input != "":
        chosen_project.priority = int(new_priority_input)

def parse_date(date_string):
    """Convert a string in the format dd/mm/yyyy to a datetime.date object."""
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()



if __name__ == "__main__":
    main()