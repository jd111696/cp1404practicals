import random

def main():
    menu = '''(G)et a valid score (must be 0-100 inclusive)
        (P)rint result (copy or import your function to determine the result from score.py)
        (S)how stars (this should print as many stars as the score)
        (Q)uit'''
    choice = input("Please select a choice from the menu: ")
    while choice != "Q":
        if choice == "G":
            score = random.randint(0,100)
            print("Score: ", score)
            choice = input("Please select a choice from the menu: ")
            while choice != "G":
                if choice == "P":
                    print("Your score is", calc_score(score))
                    choice = input("Please select a choice from the menu: ")
                elif choice == "S":
                    print("*" * score)
                    choice = input("Please select a choice from the menu: ")
        elif choice == "P" or choice == "S":
            print("Please get a score first.")
            choice = input("Please select a choice from the menu: ")
        else:
            print("Invalid choice")
            choice = input("Please select a choice from the menu: ")
    print("Thank you. Goodbye.")

def calc_score(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()