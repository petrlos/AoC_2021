#Advent of Code 2021: Day 23
from collections import deque

def scoreCounter(start, end, letter):
    multiplier = {"A":1, "B":10, "C":100, "D":1000}
    steps = sum(abs(val1-val2) for val1, val2 in zip(start,end)) + 1
    return steps * multiplier[letter]

def mazeCompleted(letters):
    for key, positions in letters.items():
        if homes[key] != positions:
            return False
    return True

with open("data.txt") as file:
    lines = file.read().splitlines()

letters = {"A":set(), "B":set(), "C":set(), "D":set()}
maze = {}
for row, line in enumerate(lines):
    for column, char in enumerate(line):
        if char == ".":
            maze[(row, column)] = char
        elif char in list("ABCD"):
            letters[char].add((row, column))
            maze[(row, column)] = "."

homes = {"A":set(), "B":set(), "C":set(), "D":set()}
for letter, column in zip(list("ABCD"), [3,5,7,9]):
    for row in [2,3,4,5]:
        homes[letter].add((row, column))

queue = deque([letters])

print(queue[0])

while queue:
    currentState = queue[0]
    for letter, locations in currentState.items():
        for location in locations:
            ...
    queue.popleft()


start = (5,6)
end = (1,8)
print(scoreCounter(start, end, "C"))