#Advent of Code 2021: Day 24
from icecream import ic

def perform_block(w, commands):
    operations = {
        "add": lambda a, b, registers: registers.update({a: registers[a] + b}),
        "mul": lambda a, b, registers: registers.update({a: registers[a] * b}),
        "div": lambda a, b, registers: registers.update({a: registers[a] // b}),
        "mod": lambda a, b, registers: registers.update({a: registers[a] % b}),
        "eql": lambda a, b, registers: registers.update({a: 1 if registers[a] == b else 0})
    }
    registers["w"] = w #first input line
    for command in commands.splitlines():
        inst, first, second = command.split(" ")
        if second.isalpha():
            second = registers[second]
        else:
            second = int(second)
        operations[inst](first, second, registers)

#MAIN
with open("data.txt") as file:
    lines = file.read().split("inp w\n")

for z in range(-1000,100000):
    for w in range(1, 10):
        registers = {'x': 0, 'y': 0, 'z': z }
        perform_block(w, lines[-1])
        if registers["z"] == 0:
            print(w, z, registers)