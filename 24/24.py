#Advent of Code 2021: Day 24
from itertools import product

def extract_constraints(lines):
    blocks = []
    for i in range(14):
        block = lines[i * 18 : (i + 1) * 18]
        A = int(block[4].split()[-1])   # div z A
        B = int(block[5].split()[-1])   # add x B
        C = int(block[15].split()[-1])  # add y C
        blocks.append((A, B, C))

    stack = []
    constraints = []

    for i, (A, B, C) in enumerate(blocks):
        if A == 1:
            stack.append((i, C))
        elif A == 26:
            j, Cj = stack.pop()
            offset = Cj + B
            constraints.append((j, i, offset))  # means: w[i] == w[j] + offset

    return constraints

def number_valid(ciphers, constraints):
    number = [0] * 14
    for cipher, constraint in zip(ciphers, constraints):
        first, second, diff = constraint
        number[first] = cipher
        number[second] = cipher + diff
    if all(0 < cipher < 10 for cipher in number):
        return number, True
    else:
        return 0, False

def check_all_ciphers(constraints):
    cipher_set = product(reversed(range(1, 10)), repeat=7)
    #generate group of 7 numbers 1-9, count the remaining 7 numbers depending on constraints, check
    results = []
    for ciphers in cipher_set:
        number, valid = number_valid(ciphers, constraints)
        if valid:
            results.append(number)

    print("Part 1:", "".join([str(num) for num in max(results)]))
    print("Part 2:", "".join([str(num) for num in min(results)]))

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

constraints = extract_constraints(lines)

#check_all_ciphers(constraints)

results = [(0,0)] * 14
for constraint in constraints:
    first, second, diff = constraint
    if diff > 0:
        results[first] = (1,9-diff)
        results[second] = (1+diff, 9)
    else:
        results[first] = (9, 1-diff)
        results[second] = (9+diff, 1)

min_number = ""
max_number = ""
for pair in results:
    min_number += str(min(pair))
    max_number += str(max(pair))

print(max_number)
print(min_number)