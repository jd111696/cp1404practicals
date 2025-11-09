""" CP1404 - Project Management

Estimated time: 60 minutes
Actual time:     minutes
"""

from project import Project

DEFAULT_FILENAME = "projects.txt"


def main():
    """Load projects from the default file and display them."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    for project in projects:
        print(project)


def load_projects(filename):
    """Load projects from a tab-delimited file, keeping dates as strings."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


if __name__ == "__main__":
    main()