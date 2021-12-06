#Advent of Code 2021: Day 6
from copy import deepcopy
from datetime import datetime
start = datetime.now()

def countXDays(starter, X):
    oldstatus = {}
    newstatus = {}
    for i in range(9):
        if i in starter:
            oldstatus.setdefault(i, starter.count(i))
        else:
            oldstatus.setdefault(i, 0)
        newstatus.setdefault(i, 0)
    for ticker in range(X):
        for i in range(9):
            newstatus[i] = oldstatus[(i + 1) % 9]
        newstatus[6] += oldstatus[0]
        oldstatus = deepcopy(newstatus)
    return sum(oldstatus.values())

#MAIN
with open("test.txt") as file:
    starter = [int(x) for x in file.read().split(",")]

#start

print("Task 1:", countXDays(starter, 80))
print("Task 2:", countXDays(starter, 256))

print("Total runtime:", datetime.now() - start)