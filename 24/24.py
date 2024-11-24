#Advent of Code 2021: Day 24
from icecream import ic
class Node:
    def __int__(self, final_z, input_z, w):
        self.w = w
        self.final_z = final_z
        self.input_z = input_z
        self.parent = None

def parse_block(single_block):
    block = dict()
    block["z_div"] = int(single_block[3].split(" ")[-1])
    block["x_check"] = int(single_block[4].split(" ")[-1])
    block["y_add"] = int(single_block[14].split(" ")[-1])
    return block

def perform_single_block(w, z, block):
    x = z % 26
    z //= block["z_div"]
    if x != w - block["x_check"]:
        z = 26 * z + w + block["y_add"]
    return z

#MAIN
with open("data.txt") as file:
    lines = file.read().split("inp w\n")

blocks = []
for line in lines[1:]: #first instruction is "inp w" - split creates an empty block of instructions
    block = parse_block(line.splitlines())
    blocks.append(block)

number = "41171183141291"
z = 0
for w, block in zip(number, blocks):
    z = perform_single_block(int(w), z, block)

print(z)