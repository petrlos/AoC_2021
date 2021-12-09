#Advent of Code 2021: Day 9
from math import prod
from datetime import datetime
start = datetime.now()

def tupleSum(a,b): #my favourite function to work with coords
    return tuple([x + y for x, y in zip(a,b)])

def allNeighboursLower(coord): #check, if all neighbours are bigger
    for direction in directions:
        neighbour = tupleSum(direction, coord)
        if neighbour in cave.keys():
            if cave[neighbour] <= cave[coord]:
                return False
    return True

def spreadBorders(start): #find all neighbours, which are NOT = 9
    newCoords = []
    for direction in directions:
        notBorder = tupleSum(direction, start)
        if notBorder in cave.keys():
            if cave[notBorder] != 9:
                newCoords.append(notBorder)
    return newCoords

def checkBasin(start): #something like BFS
    basin = [start]
    queue = [start]
    while len(queue) > 0:
        newCoords = spreadBorders(queue[-1])
        queue.pop(-1)
        for coord in newCoords:
            if coord not in basin:
                queue.append(coord)
                basin.append(coord)
    for coord in basin: #everything in closed basin must be checked, so that each basin comes only once
        caveBasinChecked[coord] = True
    return len(basin)

#MAIN
with open("data.txt") as file:
    data = file.read().splitlines()

directions = [(0,-1), (0,1), (-1,0), (1,0)]#UDLR
cave = {} #basic dictionary - coord:value
caveBasinChecked = {} #dictionary for task2: coord: True/False - basin checked/not checked
for x, row in enumerate(data):
    for y, char in enumerate(row):
        cave[(x,y)] = int(char)
        caveBasinChecked[(x,y)] = False

#Task1
riskLvl = 0
for coord in cave.keys():
    if allNeighboursLower(coord):
        riskLvl += cave[coord] + 1
print("Task 1:", riskLvl)

#Task2:
results = []
for coord in cave.keys():
    if not caveBasinChecked[coord]:
        if cave[coord] != 9:
            size = checkBasin(coord)
            results.append(size)
results = sorted(results, reverse=True)

print("Task 2:",prod(results[0:3]))
print("Runtime:", datetime.now() - start)