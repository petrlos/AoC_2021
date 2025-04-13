#Advent of Code 2021: Day 16
class Node:
    def __init__(self, version, type, pointer, value=0):
        self.version = version
        self.type = type
        self.packet_start = pointer
        self.value = value #result of operations of children
        self.children = None if type == 4 else [] #literal value has no children
        self.subpackets = None
        self.length = None
        self.subpacket_end = None

    def __repr__(self):
        return f"Vs:{self.version}, Tp:{self.type}, Val:{self.value}, Children: {self.children}"

    def add_child(self, packet):
        self.children.append(packet)

def convert_hex_to_bin(hex_num):
    return "".join(bin(int(c, 16))[2:].zfill(4) for c in hex_num)

def decode_literal_value(pointer):
    value_bits = ""
    while True:
        group = bin_number[pointer:pointer+5]
        value_bits += group[1:]
        pointer += 5
        if group[0] == "0":
            break
    return int(value_bits, 2), pointer

def add_to_stack(pointer):
    vs = int(bin_number[pointer:pointer+3], 2)
    type = int(bin_number[pointer+3:pointer+6], 2)
    node = Node(vs, type, pointer)
    pointer += 6 #move past version and type
    if type == 4:
        node.value, pointer = decode_literal_value(pointer)
    else:
        if bin_number[pointer] == "0": #next 15 bits define how long is subpacket
            node.length = int(bin_number[pointer+1:pointer+16], 2)
            pointer += 16
            node.subpacket_end = pointer + node.length
        else: #next 11 bits define how many subpackets in this subpacket
            node.subpackets = int(bin_number[pointer+1:pointer+12])
            pointer += 12
    return pointer, node

def generate_tree(bin_number):
    tree = []
    stack = []

    versions = 0
    pointer = 0
    while pointer + 7 < len(bin_number):
        if len(stack) == 0:
            pointer, added = add_to_stack(pointer)
            tree.append(added)
            stack.append(added)
            versions += added.version
        else:
            current = stack[-1]
            if current.length is not None:
                if pointer >= current.subpacket_end:
                    consumed = pointer - current.packet_start
                    if consumed >= current.length + 6:
                        stack.pop()
                        if stack:
                            stack[-1].add_child(current)
                        continue

            if current.subpackets is not None:
                if len(current.children) >= current.subpackets:
                    stack.pop()
                    if stack:
                        stack[-1].add_child(current)
                    continue
            pointer, added = add_to_stack(pointer)
            current.add_child(added)
            versions += added.version
    return tree, versions

#MAIN

with open("test_2.txt") as file:
    hex_numbers = file.read().splitlines()

bin_number = convert_hex_to_bin(hex_numbers[0])
print(hex(int(bin_number, 2))[2:], "\n", bin_number)

tree, versions_sum = generate_tree(bin_number)
print("Part 1:", versions_sum)