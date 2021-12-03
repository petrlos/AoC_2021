#Advent of Code 2021: Day 3
from collections import Counter

def findMostCommonNumber(column):
    occurenceCount = Counter(column)
    if occurenceCount["1"] >= occurenceCount["0"]:
        return "1"
    else:
        return "0"

def numbersRemaining(numbers):
    counter = 0
    for number, status in numbers.items():
        if status:
            counter += 1
    return counter

#MAIN:
with open("data.txt") as file:
    lines = file.read().splitlines()

#Task1:
columns = zip(*lines[::-1]) #rotate by 90deg - easier to walk through
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

#Task2:
numbers = {}
for number in lines:
    numbers.setdefault(number, True)

position = 0
while numbersRemaining(numbers) > 1:
    subString = ""
    for number in numbers.keys():
        if numbers[number]:
            subString += number[position]
    mostCommon = findMostCommonNumber(subString)
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
    mostCommon = findMostCommonNumber(subString)
    for number in numbers.keys():
        if numbers[number]:
            if number[position] == mostCommon:
                numbers[number] = False
    position += 1

for number in numbers.keys():
    if numbers[number]:
        CO2ScrubRating = int(number,2)

print("Task 2:", oxGenRating*CO2ScrubRating)