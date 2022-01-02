#Advent of Code 2021: Day 19
from copy import deepcopy

def parseData(lines):
    scanner, scanners = [], []
    for line in lines:
        if "scanner" in line:
            scanner = []
        elif line == "":
            scanners.append(scanner)
        elif "," in line:
            numbers = [int(x) for x in line.split(",")]
            scanner.append(numbers)
    return scanners

def rotateByY(input, index):
    x, y, z = input
    rotateByYDict = {0:[x,y,z], 1:[-x,y,-z], 2:[-z, y, x], 3:[z, y, -x]}
    return rotateByYDict[index]

def rotateToOtherSide(input, index):
    x, y, z = input
    rotateToOtherSideDict = {0:[x, y, z], 1:[y, z, x], 2:[ z, -y, x],
                             3:[x, -z,y], 4:[z, x, y], 5:[-x,-z, y]}
    return rotateToOtherSideDict[index]

#MAIN:
with open("test2.txt") as file:
    lines = file.read().splitlines()

scanners = parseData(lines)


for scanner in scanners:
    for beacon in scanner:
        for sideRotate in range(6):
            scannerRotated= rotateToOtherSide(beacon, sideRotate)
            print(sideRotate, end=" ")
            for rotateY in range(4):
                scannerRotatedY = rotateByY(scannerRotated, rotateY)
                print(scannerRotatedY, end=" ")
            print(" ")