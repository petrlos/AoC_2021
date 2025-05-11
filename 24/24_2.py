#Advent of Code 2021: Day 24

def perform_block(id, w, values):
    def decode(var):
        return values[var] if var.isalpha() else int(var)
    block = lines[id*18+1: (id*18)+18]
    values["w"] = w
    for line in block:
        instr, first, second = line.split(" ")
        values[first] = instructions[instr](decode(first), decode(second))
    return values

def check_whole_number(number, values):
    for block_id, num in enumerate(number):
        values = perform_block(block_id, int(num), values)
    return values["z"] == 0

#MAIN

with open("data.txt") as file:
    lines = file.read().splitlines()

instructions = {
    "add": lambda a, b: a + b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a // b,
    "mod": lambda a, b: a % b,
    "eql": lambda a, b: int(a == b),
}


values = {"x":0, "y":0, "z":0, "w":0}

