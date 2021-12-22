#Advent of Code 2021: Day 20
import numpy
from copy import deepcopy

def slice(midPoint, array):
    row, column = midPoint
    cutOfRows = array[[row - 1, row, row + 1], :]
    cutOfColumns = cutOfRows[:, [column - 1, column, column + 1]]
    return cutOfColumns

def extendGrid(grid, step):
    #adds a frame allong a grid for simplier calculations
    size, size = grid.shape
    newGrid = numpy.zeros((size+2, size+2))
    if step % 2 == 1:
        newGrid += 1
    for row in range(size):
        for column in range(size):
            newGrid[row+1, column+1] = grid[row, column]
    return newGrid

def decode(cutOf):
    result = ""
    for x in range(3):
        for y in range(3):
            result += str(int(cutOf[x,y]))
    return int(result, 2)

#MAIN
with open("data.txt") as file:
    input = file.read().splitlines()

iea = {} #image enhancement algorithm
for index, char in enumerate(input[0].replace("#", "1").replace(".", "0")):
    iea[index] = char

size = len(input[2:])
grid = numpy.zeros((size, size), int)

#read input grid
for row, line in enumerate(input[2:]):
    for column, char in enumerate(line):
        if char == "#":
            grid[row, column] = 1

#initial extend:
grid = extendGrid(grid, 0)

iterations = 50
for step in range(iterations):
    grid = extendGrid(grid, step)
    print(grid, "\n")
    newMaxX, newMaxY = grid.shape
    newGrid = numpy.zeros((newMaxX, newMaxY), int)
    if step % 2 == 0: #because on even step == after odd step is everything lit up
        newGrid += 1
    for row in range(1,newMaxX-1):
        for column in range(1,newMaxY-1):
            cutOf = slice((row, column),grid)
            decoded = decode(cutOf)
            newGrid[row, column] = int(iea[decoded])
    grid = deepcopy(newGrid)

print(grid.shape)
print("Result of {0} iterations:".format(iterations), numpy.sum(grid))
print("Should be: 5275")