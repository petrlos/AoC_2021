#Advent of Code 2021: Day 2 vs. 2
def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

with open("data.txt") as file:
    instructions = file.read().splitlines()

task1, task2 = (0,0), (0,0) #horizontal, vertical
aim = 0
for instruction in instructions:
    direction, step = instruction.split(" ")
    if "f" in direction:
        task1 = tupleSum(task1, (int(step), 0))
        task2 = tupleSum(task2, (int(step), int(step)*aim))
    elif "d" in direction:
        task1 = tupleSum(task1, (0, int(step)))
        aim += int(step)
    elif "u" in direction:
        task1 = tupleSum(task1, (0, -int(step)))
        aim -= int(step)

print("Task 1: {0} coords, {1} product".format(task1, task1[0]*task1[1]))
print("Task 2: {0} coords, {1} product".format(task2, task2[0]*task2[1]))