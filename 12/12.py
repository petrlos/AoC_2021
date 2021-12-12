#Advent of Code 2021: Day 12
from collections import deque
from collections import Counter

def findNextCave(location):
    destinations = deque()
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
        if max(smallCavesCounter) > 2:
            return False
        if smallCavesCounter.count(2) > 1:
            return False
    return True

def task1(start):
    queue = [[start]]
    completedLegalPaths = []
    while queue:
        for _ in range(len(queue)):
            path = queue[0]
            newCaves = findNextCave(path[-1])
            newPaths = []
            for newCave in newCaves:
                newPath = path + [newCave]
                newPaths.append(newPath)
            queue += newPaths
            queue.pop(0)
        for index, path in enumerate(queue):
            if pathCompleted(path):
                completedLegalPaths.append(path)
                queue[index] = "delete"
            if not smallCaveVisitedMaxOnce(path):
                queue[index] = "delete"
        queue = list(filter(lambda x: x != "delete", queue))
    return len(completedLegalPaths)

def task2(start):
    queue = deque([[start]])
    completedLegalPaths = 0
    while queue:
        for _ in range(len(queue)):
            path = queue[0]
            newCaves = findNextCave(path[-1])
            newPaths = []
            for newCave in newCaves:
                newPath = path + [newCave]
                newPaths.append(newPath)
            queue += newPaths
            queue.popleft()
        for index, path in enumerate(queue):
            if not smallCaveTask2Checker(path):
                queue[index] = "delete"
            if pathCompleted(queue[index]):
                completedLegalPaths += 1
                queue[index] = "delete"
        queue = deque(list(filter(lambda x: x != "delete", queue)))
        print(len(queue))
    return completedLegalPaths

#MAIN
with open("test3.txt") as file:
    lines = [x.split("-") for x in file.read().splitlines()]

print("Task 1:",task1("start"))
print("Task 2:",task2("start"))