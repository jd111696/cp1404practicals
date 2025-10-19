"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(STATE_NAMES)


def main():
    short_state = input("Enter short state: ").strip().upper()
    try:
        print(STATE_NAMES[short_state])
    except KeyError:
        print("Invalid short state")

    key_width = max(len(k) for k in STATE_NAMES)
    for abbr, name in sorted(STATE_NAMES.items()):
        print(f"{abbr:{key_width}} is {name}")


if __name__ == "__main__":
    main()
