import random

def main() :
    num_scores = int(input("Please enter number of scores: "))
    with open("results.txt", "w") as file:
        for i in range(num_scores):
            score = random.randint(0,100)
            file.write(f"{score} is {calc_score(score)}\n")


def calc_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
