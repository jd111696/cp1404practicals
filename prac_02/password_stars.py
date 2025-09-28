length = 7
pwl_length = len(input("Enter a password: "))
while pwl_length < length:
    print("Password too short")
    pwl_length = len(input("Enter a password:"))
print("*" * pwl_length)