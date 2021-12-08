# Advent of Code 2021: Day 8

with open("data.txt") as file:
    lines = file.read().splitlines()

signals = []
outputs = []
for line in lines:
    signal, output = line.split(" | ")
    signals.append(signal)
    outputs.append(output)

#Task1
counter = 0
oneFourSevenEight = [2, 4, 3, 7] #segments count needed to light up this number
for output in outputs:
    numbers = output.split(" ")
    for number in numbers:
        if len(number) in oneFourSevenEight:
            counter += 1
print("Task 1: ",counter)