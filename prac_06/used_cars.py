"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note: Keep module/folder names simple (no spaces/caps) for valid imports.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use Car class."""
    my_car = Car(name="Daily", fuel=180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(name="Limo", fuel=100)
    limo.add_fuel(20)
    print(f"Limo fuel after add: {limo.fuel}")

    distance_driven = limo.drive(115)
    print(f"Limo actually drove: {distance_driven} km")
    print(limo)


if __name__ == "__main__":
    main()