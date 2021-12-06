#Advent of Code 2021: Day 6
import numpy
from copy import deepcopy
from datetime import datetime
start = datetime.now()

with open("data.txt") as file:
    starter = [int(x) for x in file.read().split(",")]

fish = numpy.array(starter)

for ticker in range(80):
    fish = fish - 1
    fish = numpy.append(fish, fish[fish < 0] + 9)
    fish = numpy.where(fish < 0, 6, fish)

print("Task 1 - 80 days using numpy: ", len(fish))
print("Naive aproach with numpy has no solution for Task 2: 256 dasy")

#start
oldstatus = {}
newstatus = {}

for i in range(9):
    if i in starter:
        oldstatus.setdefault(i, starter.count(i))
    else:
        oldstatus.setdefault(i, 0)
    newstatus.setdefault(i,0)

"""
SHAME ON ME :D
for ticker in range(256):
    newstatus[8] = oldstatus[0]
    newstatus[7] = oldstatus[8]
    newstatus[6] = oldstatus[7] + oldstatus[0]
    newstatus[5] = oldstatus[6]
    newstatus[4] = oldstatus[5]
    newstatus[3] = oldstatus[4]
    newstatus[2] = oldstatus[3]
    newstatus[1] = oldstatus[2]
    newstatus[0] = oldstatus[1]
    oldstatus = deepcopy(newstatus)"""

for ticker in range(256):
    for i in range(9):
        newstatus[i] = oldstatus[(i+1) % 9]
    newstatus[6] += oldstatus[0]
    oldstatus = deepcopy(newstatus)

print("Task 2 - 256 days:",sum(oldstatus.values()))
print("Total runtime:", datetime.now() - start)