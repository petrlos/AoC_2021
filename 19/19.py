#Advent of Code 2021: Day 19
from datetime import datetime
from itertools import combinations
start = datetime.now()

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
    for beacon in beacons:
        beaconDirectionRotated = rotateToOtherDirection(beacon, direction)
        beaconYrotated = rotateByY(beaconDirectionRotated, YAxe)
        rotatedScanner.append(beaconYrotated)
    return rotatedScanner

def correctByVektor(vektor, scanner):
    correctedScanner = []
    for beacon in scanner:
        correctedBeacon = [x + y for x,y in zip(vektor,beacon)]
        correctedScanner.append(correctedBeacon)
    return correctedScanner

def intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]

def findIntersectionOfTwoScanners(referenceScanner, scannerToRotate):
    for rotation in range(24):
        rotatedScanner = rotateCompleteScanner(scannerToRotate, rotation)
        for referenceBeacon in referenceScanner:
            for beacon in rotatedScanner:
                vektor = [x - y for x,y in zip(referenceBeacon, beacon)] #vektor to reference beacon
                correctedScanner = correctByVektor(vektor, rotatedScanner) #correct all beacons according to vector
                intersect = intersection(referenceScanner, correctedScanner) #find matching beacons
                if len(intersect) == 12:
                    print(sorted(intersect))
                    return 0

#MAIN:
with open("test.txt") as file:
    lines = file.read().splitlines()

scanners = parseData(lines)
print(len(scanners))

comb = combinations(range(len(scanners)),2)
visited = set()

#search all pairs for match of at least 12
for c in comb:
    first, second = c
    if findIntersectionOfTwoScanners(scanners[first], scanners[second]) == 0:
        #match found - add scanner ID to visited
        visited.add(first)
        visited.add(second)

# visited = paired scanners
print(len(visited))
print(sorted(list(visited)))

print(datetime.now() - start)