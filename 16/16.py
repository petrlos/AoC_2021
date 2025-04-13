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
        if self.type == 4:
            return f"Val:{self.value}"
        else:
            return f":{self.version}/{self.type}: {self.children}"

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
    vs = int(bin_number[pointer:pointer+3], 2) #first triplet
    type = int(bin_number[pointer+3:pointer+6], 2) #second triplet
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
            node.subpackets = int(bin_number[pointer+1:pointer+12], 2)
            pointer += 12
    return pointer, node

def generate_tree(bin_number):
    tree = []
    stack = []
    versions = 0 #needed for part 1
    pointer = 0
    while pointer + 7 < len(bin_number): #no new packet may be loaded
        if len(stack) == 0: #top of the tree
            pointer, added = add_to_stack(pointer)
            tree.append(added)
            stack.append(added)
            versions += added.version
        else:
            current = stack[-1]
            if current.length is not None: #subpackets are defined via length in bits
                if pointer >= current.subpacket_end: #length runs out
                    stack.pop() #remove from stack - move one branch up
                    continue
            elif current.subpackets is not None: #subpackets are defined via count
                if len(current.children) == current.subpackets: #count of subpackets reached
                    stack.pop()
                    continue
            pointer, added = add_to_stack(pointer)
            if added.type != 4: #not value? must contain other packets: add to stack
                stack.append(added)
            current.add_child(added)
            versions += added.version
    return tree, versions

def solve_node(node):
    if node.type == 0: #sum up all children
        sum_up = 0
        for child in node.children:
            sum_up += solve_node(child)
        return sum_up
    elif node.type == 1: #product of all children
        product = 1
        for child in node.children:
            product *= solve_node(child)
        return product
    elif node.type == 2: #minimum of all children
        values_list = []
        for child in node.children:
            values_list.append( solve_node(child))
        return min(values_list)
    elif node.type == 3: #maximum of all children
        values_list = []
        for child in node.children:
            values_list.append( solve_node(child))
        return max(values_list)
    elif node.type == 5: #greater than: first > second: 1 else 0
        value1 = solve_node(node.children[0])
        value2 = solve_node(node.children[1])
        return 1 if value1 > value2 else 0
    elif node.type == 6: #lesser than: first < second: 1 else 0
        value1 = solve_node(node.children[0])
        value2 = solve_node(node.children[1])
        return 1 if value1 < value2 else 0
    elif node.type == 7: #equal: first == second: 1 else O
        value1 = solve_node(node.children[0])
        value2 = solve_node(node.children[1])
        return 1 if value1 == value2 else 0
    else: # == 4
        return node.value


#MAIN

with open("data.txt") as file:
    hex_number = file.read().splitlines()

bin_number = convert_hex_to_bin(hex_number)

tree, versions_sum = generate_tree(bin_number)
print("Part 1:", versions_sum)

result = solve_node(tree[0])
print("Part 2:", result)