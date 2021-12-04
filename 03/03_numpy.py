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