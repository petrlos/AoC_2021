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
    newGrid = {}
    #copy to right
    for x in range(maxX):
        for y in range(maxY):
            for i in range(5):
                newGrid[(x+(i*maxX), y)] = grid[x,y] + i
    #copy down
    for y in range(maxY):
        for x in range(maxY*5):
            for i in range(0,5):
                newGrid[(x, y+(maxY*i))] = i + newGrid[(x,y)]
    #correct > 9
    for coord in newGrid.keys():
        while newGrid[coord] > 9:
            newGrid[coord] -= 9

    return newGrid

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid = {}
start = (0,0)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[(x,y)] = int(char)
sizeX, sizeY = x,y

grid = extendedGrid(grid, sizeX+1, sizeY+1)
sizeX = (sizeX+1) *5
sizeY = (sizeY+1) *5

distances = numpy.zeros((sizeX+1,sizeY+1))-1
distances[start] = grid[start]#startdistance

queue = set()
queue.add(start)

counter = 0
while queue:
    counter += 1 #how many coords have been checked
    if counter % 1000 == 0:
        print(counter, len(queue), datetime.now()-timerStart)
    currentStep = findNextStep(queue)
    generateNeighboursDistance(currentStep)
    queue.remove(currentStep)
    if distances[(sizeX-1, sizeY-1)] > 0:
        queue = []

result = distances[sizeX-1, sizeY-1] - distances[0,0]
print("Result:",result)
print(datetime.now() - timerStart)