
def exercise1():
    numbers = []
    count = 1
    while True:
        try:
            value = int(input(f"Number {count}: "))
        except ValueError:
            print("Invalid input; enter an integer.")
            continue
        if value < 0:
            break
        numbers.append(value)
        count += 1
    if not numbers:
        print("No valid numbers entered.")
        raise SystemExit
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average:.1f}")

def exercise2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

def repeated_strings():
    counts = {}
    while True:
        text = input()
        if text == "":
            break
        counts[text] = counts.get(text, 0) + 1
    repeated = [s for s, c in counts.items() if c > 1]
    if repeated:
        order = []
        for s in counts:
            if counts[s] > 1:
                order.append(s)
        print("Strings repeated:", ", ".join(order))
    else:
        print("No repeated strings entered")

def add_memberwise(a, b):
    result = []
    max_len = max(len(a), len(b))
    for i in range(max_len):
        left = a[i] if i < len(a) else 0
        right = b[i] if i < len(b) else 0
        result.append(left + right)
    return result

def memberwise_call():
    print(add_memberwise([1, 2, 3], [4, 5, 6]))
    print(add_memberwise([1, 2, 3], [1, 2, 3, 4]))

exercise1()
exercise2()
repeated_strings()
memberwise_call()

