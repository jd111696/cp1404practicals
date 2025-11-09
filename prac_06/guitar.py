"""CP1404/CP5632 Practical - Guitar

Estimate: 10   Start time: 10:08
Actual: 8   End time:   10:16
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self) -> int:
        return CURRENT_YEAR - self.year

    def is_vintage(self) -> bool:
        return self.get_age() >= VINTAGE_AGE
