#eg
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(0, 100, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 1):
    print(i, end=' ')
print()

#c
number_of_stars = input("Please type in any number between 1 and 20: ") #Keeping amount of stars reasonable
print("Number of Stars:", number_of_stars)
for i in range(1, int(number_of_stars)+1):
    print("*", end='')
print()

#d
n = input("Please type in any number between 1 and 20: ") #Keeping amount of stars reasonable
print("Number of Stars:", n)
for i in range(1, int(n)+1):
    print("*" * i)
print()
