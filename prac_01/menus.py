name = str(input("Enter name: "))
print("(H)ello\n(G)oodbye\n(Q)uit")
ans = str(input(">>> "))
while ans != "Q":
    if ans == "H":
        print("Hello ", name)
    elif ans == "G":
        print("Goodbye ", name)
    else:
        print("Invalid Choice.")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    ans = str(input(">>> "))
print("Finished.")