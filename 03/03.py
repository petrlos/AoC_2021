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

def createNumbersDict(lines):
    numbers = {}
    for number in lines:
        numbers.setdefault(number, True)
    return numbers

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

#Task2 - ox gen rating:
numbers = createNumbersDict(lines) #generate new dictionary of numbers
position = 0
while numbersRemaining(numbers) > 1:
    subString = "" #get substring of lines at positions
    for number, status in numbers.items(): #adds only active numbers - those with TRUE in dict
        if status:
            subString += number[position]
    mostCommon = findMostCommonNumber(subString)
    for number, status in numbers.items():
        if status:
            if number[position] != mostCommon:
                numbers[number] = False #number with less count would be deleted
    position += 1
for number, status in numbers.items():
    if status: #get the last standing number
        oxGenRating = int(number,2)

#Task2 - CO2 scrubber rating
numbers = createNumbersDict(lines) #generate new dictionary of numbers
position = 0
while numbersRemaining(numbers) > 1:
    subString = ""
    for number, status in numbers.items():
        if status:
            subString += number[position]
    mostCommon = findMostCommonNumber(subString)
    for number, status in numbers.items():
        if status:
            if number[position] == mostCommon:
                numbers[number] = False
    position += 1
for number, status in numbers.items():
    if status:
        CO2ScrubRating = int(number,2)

print("Task 2:", oxGenRating*CO2ScrubRating)