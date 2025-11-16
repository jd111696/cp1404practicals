""" CP1404 - Project """

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project with formatted date."""
        date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_string}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if the project is complete (100% or more)."""
        return self.completion_percentage >= 100

    def __lt__(self, other):
        """Compare projects by priority for sorting (lower priority number comes first)."""
        return self.priority < other.priority