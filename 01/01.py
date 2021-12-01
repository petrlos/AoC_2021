# Advent of Code 2021: Day 1
def countIncrease(depths):
    counter = 0
    for index in range(1, len(depths)):
        if depths[index] > depths[index - 1]:
            counter += 1
    return counter

with open("data.txt") as file:
    lines = file.read().splitlines()

print("AoC 2021: Day 1: ")

depths  = [int(x) for x in lines]

#task1
task1 = countIncrease(depths)
print("Task 1:",task1)

#task2:
depthsTask2 = []
for index in range(0, len(depths)-2):
    newDepth = sum(depths[index:index+3])
    depthsTask2.append(newDepth)

task2 = countIncrease(depthsTask2)
print("Task 2:",task2)