#Advent of Code 2021: Day 25
import numpy
from copy import deepcopy
from datetime import datetime

def moveSea(sea, direction):
    newSea = deepcopy(sea)
    for row in range(height):
        for column in range(width):
            if sea[row, column] == direction:
                if direction == -1: #move right
                    destination = column + 1
                    if destination > width - 1:
                        destination -= width #fall over the edge
                    if sea[row, destination] == 0:
                        newSea[row, destination] = -1
                        newSea[row, column] = 0
                elif direction == 1: #move down
                    destination = row + 1
                    if destination > height - 1:
                        destination -= height #fall over the edge
                    if sea[destination, column] == 0:
                        newSea[destination, column] = 1
                        newSea[row, column] = 0
    return newSea

#MAIN
start = datetime.now()
with open("data.txt") as file:
    lines = file.read().splitlines()

width, height = len(lines[0]), len(lines)
sea = numpy.zeros((height, width), int)

for row, line in enumerate(lines):
    for column, char in enumerate(line):
        if char == ">":
            sea[row, column] = -1 #right
        elif char == "v":
            sea[row, column] = +1 #down

done = False
steps = 0
while not done:
    steps += 1
    if steps % 100 == 0:
        print("Steps done:", steps)
    seaAfterRight = moveSea(sea, -1) #move right
    seaAfterDown = moveSea(seaAfterRight, 1) #move left
    if numpy.array_equal(seaAfterDown, sea):
        done = True
    else:
        sea = deepcopy(seaAfterDown)

print("Result:", steps)
print("Timer:", datetime.now() - start)