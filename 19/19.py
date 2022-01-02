#Advent of Code 2021: Day 19
from pprint import pprint

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
    #rotates only axe Y - 4 possible directions
    x, y, z = input
    rotateByYDict = {0:[x,y,z], 1:[-x,y,-z], 2:[-z, y, x], 3:[z, y, -x]}
    return rotateByYDict[index]

def rotateToOtherDirection(input, index):
    #rotates the whole cube - 6 possible directions
    x, y, z = input
    rotateToOtherSideDict = {0:[x, y, z], 1:[y, z, x], 2:[ z, -y, x],
                             3:[x, -z,y], 4:[z, x, y], 5:[-x,-z, y]}
    return rotateToOtherSideDict[index]

def rotateCompleteScanner(beacons, rotation):
    #finds new coords for all beacons from scanner in ONE of 24 rotations
    rotatedScanner = []
    direction, YAxe = (rotation //4), (rotation % 4)
    print(direction, YAxe)
    for beacon in beacons:
        beaconDirectionRotated = rotateToOtherDirection(beacon, direction)
        beaconYrotated = rotateByY(beaconDirectionRotated, YAxe)
        rotatedScanner.append(beaconYrotated)
    return rotatedScanner

#MAIN:
with open("test2.txt") as file:
    lines = file.read().splitlines()

scanners = parseData(lines)


for scanner in scanners:
    for rotation in range(24):
        rotatedScanner = rotateCompleteScanner(scanner, rotation)
