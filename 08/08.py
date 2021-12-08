# Advent of Code 2021: Day 8
from itertools import permutations
from datetime import datetime
start = datetime.now()

def checkPossibleDecode(signal, decodeDictionary):
    allTrue = True
    for number in signal:
        decodedNumber = ""
        for char in number:
            decodedNumber += decodeDictionary[char]
        decodedNumber = "".join(sorted(decodedNumber))
        if decodedNumber not in possibleCombinations:
            allTrue = False
    return allTrue

with open("data.txt") as file:
    lines = file.read().splitlines()

signals = []
outputs = []
for line in lines:
    signal, output = line.split(" | ")
    signals.append(signal)
    outputs.append(output)

#Task1
counter = 0
oneFourSevenEight = [2, 4, 3, 7] #segments count needed to light up this number
for output in outputs:
    numbers = output.split(" ")
    for number in numbers:
        if len(number) in oneFourSevenEight:
            counter += 1
print("Task 1: ",counter)

#Task 2:
possibleCombinations = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
                        "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"] #0123456789

allSettings = list(permutations("abcdefg"))
decodeString = "abcdefg"
decodedNumbers = []
for pair in zip(signals, outputs):
    decodeDictionary = {}
    signal, output = pair
    signal = ["".join(sorted(x)) for x in signal.split(" ")]
    output = ["".join(sorted(x)) for x in output.split(" ")]
    for setting in allSettings:
        for index, char in enumerate(setting):
            key = decodeString[index]
            decodeDictionary[char] = key
        if checkPossibleDecode(signal, decodeDictionary):
            resultNumber = ""
            for outPutNumber in output:
                resultCoded = ""
                for char in outPutNumber:
                    resultCoded += decodeDictionary[char]
                resultCoded = "".join(sorted(resultCoded))
                resultNumber += str(possibleCombinations.index(resultCoded))
            decodedNumbers.append(int(resultNumber))

print(decodedNumbers)
print(sum(decodedNumbers))
print(datetime.now() - start)