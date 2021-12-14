#Advent of Code 2021: Day 14
from collections import Counter
from datetime import datetime

with open("data.txt") as file:
    lines = file.read().splitlines()

polymer = lines[0]
rules = {}
for line in lines[2:]:
    input, output = line.split(" -> ")
    rules[input] = output

for iteration in range(10):
    start = datetime.now()
    newPolymer = polymer[0]
    for index in range(len(polymer)-1):
        element = polymer[index:index+2]
        newPolymer += rules[element] + element[1]
    polymer = newPolymer
    print(iteration, datetime.now() - start)
letterCount = Counter(polymer)
result = letterCount.most_common()[0][1] - letterCount.most_common()[-1][1]
print("Task 1:",result)