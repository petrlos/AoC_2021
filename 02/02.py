#Advent of Code 2021: Day 2
class Position:
    def __init__(self):
        self.vertical = 0
        self.horizontal = 0
        self.aim = 0
    def __str__(self):
        return "{0}, {1}".format(self.horizontal, self.vertical)
    def result(self):
        return self.vertical * self.horizontal

def task1(instruction, step, position):
    if instruction == "forward":
        position.horizontal+= int(step)
    elif instruction == "down":
        position.vertical += int(step)
    elif instruction == "up":
        position.vertical -= int(step)
    return position

def task2(instruction, step, position):
    if instruction == "forward":
        position.horizontal+= int(step)
        position.vertical += int(step) * position.aim
    elif instruction == "down":
        position.aim += int(step)
    elif instruction == "up":
        position.aim -= int(step)
    return position

with open("data.txt") as file:
    lines = file.read().splitlines()

print("AoC 2021 Day 2: ")

instructions = [x.split(" ") for x in lines]

#task1
position = Position()
for instruction in instructions:
    direction, distance = instruction
    position = task1(direction, distance, position)
task1 = position.result()
print("Task 1: ",task1)

#task2
position = Position()
for instruction in instructions:
    direction, distance = instruction
    position = task2(direction, distance, position)
task1 = position.result()
print("Task 2: ", task1)