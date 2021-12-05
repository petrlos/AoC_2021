#Advent of Code 2021: Day 5
import re
regNum = re.compile(r"\d+")

def tupleDiff(a,b):
    return tuple([x - y for x, y in zip(a,b)])

def getDirection(start, end, task=1):
    longDirection = tupleDiff(end, start)
    x, y = longDirection
    if x == 0 or y == 0:
        #only horizontal
        if x ==0:
            y = y // abs(y)
        else:
            x = x // abs(x)
        return (x,y)
    else:
        if task == 1:
            return -1
        x = x // abs(x)
        y = y // abs(y)
        return (x,y)

def getStartEnd(line):
    numbers = [int(x) for x in regNum.findall(line)]
    start = (numbers[0], numbers[1])
    end = (numbers[2], numbers[3])
    return start, end

def addCoordToPipes(coord):
    if coord not in pipes.keys():
        pipes.setdefault(coord, 1)
    else:
        pipes[coord] += 1

def generatePipes(lines, task):
    for line in lines:
        start, end = getStartEnd(line)
        direction = getDirection(start, end, task)
        if direction != -1:
            addCoordToPipes(start)
            while end != start:
                addCoordToPipes(end)
                end = tupleDiff(end, direction)
    counter = 0
    for coord, count in pipes.items():
        if count > 1:
            counter += 1
    return counter

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

pipes = {}
print("Task 1:", generatePipes(lines, 1))
pipes = {}
print("Task 2:", generatePipes(lines, 2))