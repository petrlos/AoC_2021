#Advent of Code 2021: Day 9
def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def allNeighboursLower(coord):
    for direction in directions:
        neighbour = tupleSum(direction, coord)
        if neighbour in cave.keys():
            if cave[neighbour] <= cave[coord]:
                return False
    return True

#MAIN
with open("data.txt") as file:
    data = file.read().splitlines()

directions = [(0,-1), (0,1), (-1,0), (1,0)]#UDLR
cave = {}
for x, row in enumerate(data):
    for y, char in enumerate(row):
        cave[(x,y)] = int(char)

#Task1
riskLvl = 0
for coord in cave.keys():
    if allNeighboursLower(coord):
        riskLvl += cave[coord] + 1

print("Task 1:", riskLvl)
