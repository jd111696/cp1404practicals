"""CP1404/CP5632 Practical - Guitar class.

Estimate: 20 minutes   Start time: 2055
Actual:   25 minutes   End time: 2120
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar with name, year, and cost."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation like: Gibson L-5 CES (1922) : $16,035.40."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the guitar's age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (>= VINTAGE_AGE years)."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare Guitars by year (older guitars are 'less than' newer ones)."""
        return self.year < other.year