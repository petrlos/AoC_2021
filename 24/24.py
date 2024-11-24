#Advent of Code 2021: Day 24
from icecream import ic
from datetime import datetime
time_start = datetime.now()

class Node:
    def __int__(self, final_z, input_z, w):
        self.w = w
        self.final_z = final_z
        self.input_z = input_z
        self.parent = None

def parse_block(single_block):
    #input differs only on lines 3, 4 and 14  in each block
    block = dict()
    block["z_div"] = int(single_block[3].split(" ")[-1])
    block["x_check"] = int(single_block[4].split(" ")[-1])
    block["y_add"] = int(single_block[14].split(" ")[-1])
    return block

def block_downwards(w, z, block):
    #simplified version of a program - instructions running for single block downwards
    x = z % 26
    z //= block["z_div"]
    if x != w - block["x_check"]:
        z = 26 * z + w + block["y_add"]
    return z

def check_complete_number(number):
    #runs through all instructions downwards and checks z == 0 at the end
    z = 0
    for w, block in zip(number, blocks):
        z = perform_single_block(int(w), z, block)
        ic(w, z)
    return z == 0

def block_upwards(block, z_final, w):
    #returns list of Z_s, which may be used, to get z_final
    zs = []
    x = z_final - w - block["y_add"]
    if x % 26 == 0:
        zs.append(x // 26 * block["z_div"])
    if 0 <= w - block["x_check"] < 26:
        z0 = z_final * block["z_div"]
        zs.append(w - block["x_check"] + z0)
    return zs

#MAIN
with open("data.txt") as file:
    lines = file.read().split("inp w\n")

blocks = []
for id, line in enumerate(lines[1:]): #first instruction is "inp w" - split creates an empty block of instructions
    block = parse_block(line.splitlines())
    blocks.append(block)
    ic(id, block)

#TODO: dont know ho to construct the tree backwards