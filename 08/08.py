# Advent of Code 2021: Day 8
from itertools import permutations
from datetime import datetime
start = datetime.now()

def checkPossibleDecode(signal, decodeDictionary):
    for number in signal:
        decodedNumber = ""
        for char in number:
            decodedNumber += decodeDictionary[char]
        decodedNumber = "".join(sorted(decodedNumber))
        if decodedNumber not in numberSegments:
            return False
    return True

#MAIN
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
print("Task 1:",counter)

#Task 2:
#with these segments lit up the LIST INDEX number is displayed
numberSegments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
                        "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"] #0123456789

allSettings = list(permutations("abcdefg")) #BRUTE FORCE wtf! :)
decodeString = "abcdefg" #basic combination - needed to decode
decodedNumbers = []
for pair in zip(signals, outputs):
    decodeDictionary = {}
    signal, output = pair
    signal = ["".join(sorted(x)) for x in signal.split(" ")] #all segments must be sorted, easier to compare
    output = ["".join(sorted(x)) for x in output.split(" ")]
    for setting in allSettings:
        for index, char in enumerate(setting): #decode setting, save to dictionary
            key = decodeString[index]
            decodeDictionary[char] = key
        if checkPossibleDecode(signal, decodeDictionary):
            resultNumber = ""
            for outPutNumber in output:
                resultCoded = ""
                for char in outPutNumber:
                    resultCoded += decodeDictionary[char]
                resultCoded = "".join(sorted(resultCoded))
                resultNumber += str(numberSegments.index(resultCoded))
            decodedNumbers.append(int(resultNumber))
            break # no need to check other settings

print("Task 2:",sum(decodedNumbers))
print(" ")
print(datetime.now() - start)