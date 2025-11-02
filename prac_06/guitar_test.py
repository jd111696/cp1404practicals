"""CP1404/CP5632 Practical - Simple tests for Guitar methods.

Estimate: (10)   Start time: (10:14)
Actual:   (9)   End time:   (10:23)
"""

from guitar import Guitar

def main():
    l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    print(f"{l5.name} get_age() - Expected 100. Got {l5.get_age()}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")

    print(f"{l5.name} is_vintage() - Expected True. Got {l5.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


if __name__ == "__main__":
    main()
