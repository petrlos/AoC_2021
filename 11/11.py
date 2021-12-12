#Advent of Code 2021: Day 11
from datetime import datetime
from collections import deque
start = datetime.now()

class Octopus():
    def __init__(self, value, flashed):
        self.value = value
        self.flashed = flashed

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def flash(coords):
    for direction in neighbours:
        neighbour = tupleSum(direction, coords)
        if neighbour in octopusField.keys():
            octopusField[neighbour].value += 1
            if octopusField[neighbour].value > 9:
                if octopusField[neighbour].flashed == False:
                    #if value > 9 AND not yet flashed -> comes to queue + flashed this round
                    flashQueue.append(neighbour)
                    octopusField[neighbour].flashed = True

def resetFlashes():
    #all octopuses with value > 9 become 0, all flashed = False
    for coords, octopus in octopusField.items():
        if octopus.value > 9:
            octopus.value = 0
        octopus.flashed = False

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

neighbours = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

octopusField = {}
for x, row in enumerate(lines):
    for y, column in enumerate(row):
        newOctopus = Octopus(int(column), False)
        octopusField[(x,y)] = newOctopus

flashCounter = []
for round in range(220): #because aproximately 220 rounds needed for 1st synchro flash
    newFlashes = 0
    flashQueue = deque()
    for coords, octopus in octopusField.items():
        octopus.value += 1
        if octopus.value > 9: #every octopus with value > 9 must be flashed - gets to queue + flashed = True
                              #meaning cant be flashed for second time this round
            flashQueue.append(coords)
            octopus.flashed = True
    while flashQueue: #the same as while len(flashqueue) > 0
        flash(flashQueue[0]) #flash first octopus and pop it out from queue
        newFlashes += 1
        flashQueue.popleft()
    resetFlashes()
    if newFlashes == 100: #all octopuses flashed at once
        print("Task 2 - first synchro flash:", round+1) #must be +1, because 1st round is round = 0 :)
    flashCounter.append(newFlashes)

print("Task 1 - flashes after 100 rounds:",sum(flashCounter[0:100])) #sum for first 100 flashes
print("Total runtime:", datetime.now() - start)