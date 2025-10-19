NAME_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "CORNFLOWERBLUE": "#6495ed",
    "DARKORANGE": "#ff8c00",
    "GOLD": "#ffd700",
    "HOTPINK": "#ff69b4",
    "LIGHTSALMON": "#ffa07a",
}

def main():
    while True:
        name = input("Colour name: ").strip()
        if name == "":
            break
        hex_code = NAME_TO_HEX.get(name.upper())
        if hex_code:
            print(hex_code)
        else:
            print("Invalid colour name")

if __name__ == "__main__":
    main()