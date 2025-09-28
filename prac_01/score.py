"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main() :
    score = float(input("Enter score: "))
    print(calc_score(score))
    rand_score = random.randint(0,100)
    print("Random Score: ", rand_score)
    print(calc_score(rand_score))

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