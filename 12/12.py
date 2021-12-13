#Advent of Code 2021: Day 12
from collections import deque, Counter
from datetime import datetime
start = datetime.now()

def findNextCave(location):
    destinations = []
    for line in lines:
        if location in line:
            if location == line[0]:
                destinations.append(line[1])
            else:
                destinations.append(line[0])
    return list(filter(lambda x: x != "start", destinations)) #only caves except start

def pathCompleted(path): #first node is start, last node is end
    if path[0] == "start" and path[-1] == "end":
        return True
    return False

def smallCaveVisitedMaxOnce(path):
    visitedSmallCaves = []
    for cave in path:
        if cave.islower():
            if cave not in visitedSmallCaves:
                visitedSmallCaves.append(cave)
            else:
                return False
    return True

def smallCaveTask2Checker(path):
    smallCaves = list(filter(lambda x: x.islower(), path[1:-1])) #only small caves, not start+end
    smallCavesCounter = list(Counter(smallCaves).values())
    if len(smallCavesCounter):
        if max(smallCavesCounter) > 2: #max visit for single small cave is 2
            return False
        if smallCavesCounter.count(2) > 1: #there may be two small caves with 2 visits
            return False
    return True

def task1(start):
    queue = deque([[start]])
    completedLegalPaths = []
    while queue:
        for _ in range(len(queue)):
            path = queue[0]
            newCaves = findNextCave(path[-1])
            for newCave in newCaves:
                newPath = path + [newCave]
                if smallCaveVisitedMaxOnce(newPath):
                    if pathCompleted(newPath):
                        completedLegalPaths.append(newPath)
                    else:
                        queue.append(newPath)
            queue.popleft()
    return len(completedLegalPaths)

def task2(start):
    queue = deque([[start]])
    completedLegalPaths = 0
    while queue:
        for _ in range(len(queue)):
            path = queue[0]
            newCaves = findNextCave(path[-1])
            for newCave in newCaves:
                newPath = path + [newCave]
                if smallCaveTask2Checker(newPath):
                    if pathCompleted(newPath):
                        completedLegalPaths += 1
                    else:
                        queue.append(newPath)
            queue.popleft()
        print("Paths in queue remaining:", len(queue))
    return completedLegalPaths

#MAIN
with open("data.txt") as file:
    lines = [x.split("-") for x in file.read().splitlines()]

print("Task 1:",task1("start"))
print("Runtime only Task1", datetime.now() - start)
print("Task 2:",task2("start"))
print("Runtime Task1 + Task2", datetime.now() - start)