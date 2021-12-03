#Advent of Code 2021: Day 3
from collections import Counter

def findMostCommonNumber(column):
    occurenceCount = Counter(column)
    return occurenceCount.most_common(1)[0][0]

with open("data.txt") as file:
    lines = file.read().splitlines()

columns = zip(*lines[::-1])

#Task1
gamaRate = ""
epsilonRate = ""
for column in columns:
    newNumber = findMostCommonNumber(column)
    gamaRate += newNumber
    if newNumber == "0":
        epsilonRate += "1"
    else:
        epsilonRate += "0"

print("Task 1:", int(gamaRate, 2) * int(epsilonRate, 2))