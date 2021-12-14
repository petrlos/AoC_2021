#Advent of Code 2021: Day 14
from collections import defaultdict, Counter
from copy import deepcopy
from datetime import datetime

def task1naive(polymer):
    for iteration in range(10):
        newPolymer = polymer[0]
        for index in range(len(polymer) - 1):
            element = polymer[index:index + 2]
            newPolymer += rules[element] + element[1]
        polymer = newPolymer
    letterCount = Counter(polymer)
    return letterCount.most_common()[0][1] - letterCount.most_common()[-1][1]

def unlimitedIterations(polymer, iterations):
    elements = defaultdict(int)
    pairs = defaultdict(int)
    for char in polymer:
        elements[char] += 1
    for index in range(len(polymer) - 1):
        pairs[polymer[index:index + 2]] += 1
    for i in range(iterations):
        newPairs = defaultdict(int)
        for pair, count in pairs.items():
            pair1, pair2 = pair[0] + rules[pair], rules[pair] + pair[1]
            newPairs[pair1] += count
            newPairs[pair2] += count
            elements[rules[pair]] += count
        pairs = deepcopy(newPairs)
    results = list(elements.values())
    return max(results) - min(results)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

polymer = lines[0]
rules = {}
for line in lines[2:]:
    input, output = line.split(" -> ")
    rules[input] = output

#each one separate timer
start = datetime.now()
print("Task 1 naive:",task1naive(polymer))
print("Runtime:", datetime.now() - start)

start = datetime.now()
print("Task 1 quick:", unlimitedIterations(polymer, 10))
print("Runtime:", datetime.now() - start)

start = datetime.now()
print("Task 2 quick:", unlimitedIterations(polymer, 40))
print("Runtime:", datetime.now() - start)