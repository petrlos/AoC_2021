#Advent of Code 2021: Day 19 vs. 2
from icecream import ic
from collections import defaultdict
import re

class Scanner:
    def __init__(self, lines):
        self.beacons = defaultdict(list) #each dict index 0..23 contains all beacons rotated in same way
        lines = lines.splitlines()
        for line in lines[1:]:
            numbers = tuple(map(int, (re.findall(r"-?\d+", line))))
            # generate all possible 24 rotations of this coord
            # each "side" may face up in 6 different ways * 4 rotated along Z axis
            for i in range(24):
                step1 = self._rotate_in_6_dir(numbers, i)
                step2 = self._rotate_by_z(step1, i)
                self.beacons[i].append(step2) #add this rotation to list of beacons

        self.offset = None #if none, beacons not yet matched with other scanner/s

    def generate_fingerprints(self):
        #generate squared distances (to avoid float by sqrt) between all pairs of beacons
        #cant be in init, because after new scanner is added, new fingerprints must be generated
        #fingerprints are for all 24 rotations the same
        self.finger_prints = set()
        for i in range(len(self.beacons[0])-1):
            for j in range(i+1, len(self.beacons[0])):
                x1, y1, z1 = self.beacons[0][i]
                x2, y2, z2 = self.beacons[0][j]
                squared_dist = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
                self.finger_prints.add(squared_dist)

    def _rotate_by_z(self, coord, count):
        x, y, z = coord
        for _ in range(count % 4):
            x, y = -y, x
        return (x, y, z)

    def _rotate_in_6_dir(self, coord, count):
        x, y, z = coord
        rotation = [
            ( x,  y,  z),
            ( y,  z,  x),
            (-z, -x,  y),
            ( z, -x, -y),
            (-y, -x, -z),
            (-y,  z, -x)
        ]
        return rotation[count // 4]

#MAIN
with open("test.txt") as file:
    input_data = file.read().split("\n\n")

scanners = list()

for list_of_beacons in input_data:
    scanner = Scanner(list_of_beacons)
    scanner.generate_fingerprints()
    scanners.append(scanner)
