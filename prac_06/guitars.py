"""CP1404/CP5632 Practical - Manage a list of Guitars using get-item pattern (no while loops).

Estimate: (20)   Start time: (10:26)
Actual:   (18)   End time:   (10:44)
"""

from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    names = []
    for i in range(100):
        name = input("Name: ").strip()
        if name == "":
            break
        year_text = input("Year: ").strip()
        cost_text = input("Cost: $").strip()
        try:
            year = int(year_text)
            cost = float(cost_text)
        except ValueError:
            print("Invalid year or cost; skipping this entry.")
            continue
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        names.append(name)
        print(f"{guitar} added.\n")

    print("\nThese are my guitars:")
    for i in range(len(guitars)):
        guitar = guitars[i]
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
