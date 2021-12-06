#Advent of Code 2021 Day 3 using numpy
import numpy
from collections import Counter

with open("test.txt") as file:
    lines = [list(x) for x in file.read().splitlines()]

numbers = numpy.array(lines)

height, length = numbers.shape

firstNumber = ""
secondNumber = ""
for index in range(length):
    mostCommon = Counter(numbers[:,index]).most_common(2)
    firstNumber += mostCommon[0][0] #takes the most common bit
    secondNumber += mostCommon[-1][0] #takes the least common bit

print(int(firstNumber, 2) * int(secondNumber, 2))

#Task2
currentColumn = 0
while numbers.shape[0] > 1:
    numbers = numbers[numbers[:, currentColumn].argsort()]
    mostCommon = Counter(numbers[:,currentColumn]).most_common(1)[0]
    mostCommonNumber, count = mostCommon
    if count * 2 == numbers.shape[0]:
        numbers = numbers[-count:]
    elif mostCommonNumber == "1":
        numbers = numbers[-count:]
    elif mostCommonNumber == "0":
        numbers = numbers[:count-1]
    currentColumn += 1
    print("After column {} checked".format((currentColumn)))
    print(numbers, "\n")