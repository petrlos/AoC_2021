#Advent of Code 2021: Day 15 - Dijkstra
from datetime import datetime
timerStart = datetime.now()
import numpy

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def findNextStep(queue): #return coords from queue with minimal distance
    minimalDistanceInQueue = min([distances[item] for item in queue])
    result = numpy.where(distances == minimalDistanceInQueue)
    listOfCoordinates = list(zip(result[0], result[1]))
    for coord in listOfCoordinates:
        if coord in queue:
            return coord

def generateNeighboursDistance(coord):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UDLR
    for direction in directions:
        newNeighbour = tupleSum(coord, direction)
        if newNeighbour in grid.keys():
            if distances[newNeighbour] == -1:
                distances[newNeighbour] = grid[newNeighbour] + distances[coord]
                queue.add(newNeighbour)

#needed for Task2:
def extendedGrid(grid, maxX, maxY):
    ...
#TODO: extended grid not working

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid = {}
start = (0,0)

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        grid[(x,y)] = int(char)
sizeX, sizeY = x,y

#extendedGrid(grid, sizeX, sizeY)

distances = numpy.zeros((sizeX+1,sizeY+1))-1
distances[start] = grid[start]#startdistance

queue = set()
queue.add(start)

while queue:
    currentStep = findNextStep(queue)
    generateNeighboursDistance(currentStep)
    queue.remove(currentStep)
    if distances[(sizeX, sizeY)] > 0:
        queue = []

result = distances[sizeX, sizeY] - distances[0,0]
print("Result:",result)
print(datetime.now() - timerStart)