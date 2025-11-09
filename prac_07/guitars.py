"""CP1404 Practical - Guitars

Estimate: 20 minutes   Start time: 2055
Actual:   25 minutes   End time: 2120
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read, display, add, sort, and save guitars."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    guitars += get_new_guitars()

    guitars.sort()
    print("\nSorted by year:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display all guitars in a formatted list."""
    print("\nThese are your guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitars():
    """Ask the user to enter new guitars and return a list of them."""
    new_guitars = []
    print("\nEnter your new guitars (press Enter to stop):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save the list of guitars to the CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    print(f"\nAll guitars saved to {filename}")


if __name__ == "__main__":
    main()