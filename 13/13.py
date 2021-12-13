#Advent of Code 2021: Day 13
import re
regNum = re.compile(r"\d+")

def drawOrigami(origami):
    origami = list(origami)
    for columnn in range(sizeY):
        for row in range(sizeX):
            if (row, columnn) in origami:
                print("#", end="")
            else:
                print(" ", end="")
        print(" ")
    print(" ")

def foldOrigami(origami, axis, foldingLine):
    newOrigami = set()
    for coord in origami:
        x, y = coord
        if axis == "x": #fold vertically
            if x > foldingLine:
                x = foldingLine - abs(foldingLine - x)
        else: #axis == y - fold horizantally
            if y > foldingLine:
                y = foldingLine - abs(foldingLine - y)
        newOrigami.add((x,y))
    return list(newOrigami)

def getSize(origami):
    sizeX, sizeY = [], []
    for coord in origami:
        x, y = coord
        sizeX.append(x)
        sizeY.append(y)
    sizeX = max(sizeX) + 1
    sizeY = max(sizeY) + 1
    return sizeX, sizeY

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

origami = []
foldingInstructions = []
for line in lines:
    if line != "":
        if "fold" in line:
            number = int(regNum.findall(line)[-1])
            if "x" in line:
                fold = ["x",number]
            else:
                fold = ["y",number]
            foldingInstructions.append(fold)
        if "," in line:
            coords = tuple(int(x) for x in line.split(","))
            origami.append(coords)

#get origamin size
sizeX, sizeY = getSize(origami)

dots = []
for instruction in foldingInstructions:
    axis, line = instruction
    origami = foldOrigami(origami, axis, line)
    dots.append(len(origami))

sizeX, sizeY = getSize(origami)
print("Task 1:",dots[0]) #only first count is needed
print("Task 2 (read the letters):")
drawOrigami(origami)