
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

first_initials = [name[0] for name in names]
print(first_initials)

full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

a_names = [name for name in names if name.startswith('A')]
print(a_names)

print(" ".join(sorted(names)))

lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(s) for s in almost_numbers]
print(numbers)

greater_than_nine = [n for n in numbers if n > 9]
print(greater_than_nine)

last_names_long = ", ".join([n.split()[1] for n in full_names if len(n) > 11])
print(last_names_long)