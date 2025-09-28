
def main() :
    length = 7
    pwl_length = get_password(length)
    print_asterisks(pwl_length)


def print_asterisks(pwl_length: int):
    print("*" * pwl_length)


def get_password(length: int) -> int:
    pwl_length = len(input("Enter a password: "))
    while pwl_length < length:
        print("Password too short")
        pwl_length = len(input("Enter a password:"))
    return pwl_length


main()

