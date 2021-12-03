#Advent of Code 2021: Day 3
from collections import Counter

def findMostCommonNumber(column, preference):
    occurenceCount = Counter(column)
    if occurenceCount["1"] > occurenceCount["0"]:
        return "1"
    elif occurenceCount["1"] == occurenceCount["0"]:
        return "1"
    elif occurenceCount["1"] < occurenceCount["0"]:
        return "0"

def numbersRemaining(numbers):
    counter = 0
    for status in numbers.keys():
        if numbers[status]:
            counter += 1
    return counter

with open("data.txt") as file:
    lines = file.read().splitlines()

columns = zip(*lines[::-1])

#Task1
gamaRate = ""
epsilonRate = ""
for column in columns:
    newNumber = findMostCommonNumber(column, "")
    gamaRate += newNumber
    if newNumber == "0":
        epsilonRate += "1"
    else:
        epsilonRate += "0"

print("Task 1:", int(gamaRate, 2) * int(epsilonRate, 2))

numbers = {}
for number in lines:
    numbers.setdefault(number, True)

position = 0
while numbersRemaining(numbers) > 1:
    subString = ""
    for number in numbers.keys():
        if numbers[number]:
            subString += number[position]
    mostCommon = findMostCommonNumber(subString, "1")
    for number in numbers.keys():
        if numbers[number]:
            if number[position] != mostCommon:
                numbers[number] = False
    #printRemaining(numbers)
    position += 1

for number in numbers.keys():
    if numbers[number]:
        oxGenRating = int(number,2)

numbers = {}
for number in lines:
    numbers.setdefault(number, True)

position = 0
while numbersRemaining(numbers) > 1:
    subString = ""
    for number in numbers.keys():
        if numbers[number]:
            subString += number[position]
    mostCommon = findMostCommonNumber(subString, "0")
    for number in numbers.keys():
        if numbers[number]:
            if number[position] == mostCommon:
                numbers[number] = False
    position += 1

for number in numbers.keys():
    if numbers[number]:
        CO2ScrubRating = int(number,2)

print("Task 2:", oxGenRating*CO2ScrubRating)