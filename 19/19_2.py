#Advent of Code 2021: Day 19 vs. 2
from collections import defaultdict
import re
from datetime import datetime
time_start = datetime.now()

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

        self.finger_prints = set() #fingerprints would be generated separately

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

def generate_fingerprints(beacons):
    #generate squared distances (to avoid float by sqrt) between all pairs of beacons
    #cant be in init, because after new scanner is added, new fingerprints must be generated
    finger_prints = set()
    for i in range(len(beacons)-1):
        for j in range(i+1, len(beacons)):
            x1, y1, z1 = beacons[i]
            x2, y2, z2 = beacons[j]
            squared_dist = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
            finger_prints.add(squared_dist)
    return finger_prints

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def check_offset(coord, rotated_beacons):
    for aligned_coord in beacons_aligned:
        offset = tuple([x - y for x, y in zip(aligned_coord, coord)])
        beacons_offset = set()
        for beacon in rotated_beacons:
            beacon_offset = tuple([x + y for x, y in zip(offset, beacon)])
            beacons_offset.add(beacon_offset)
        if len(beacons_offset & set(beacons_aligned)) >= 12:
            return offset, beacons_offset
    return -1, -1

#MAIN
with open("data.txt") as file:
    input_data = file.read().split("\n\n")

scanners = list()

for list_of_beacons in input_data:
    scanner = Scanner(list_of_beacons)
    scanner.finger_prints = generate_fingerprints(scanner.beacons[0])
    #take the 0th rotation only - all fingerprints are the same
    scanners.append(scanner)

beacons_aligned = list() #add beacons from 0th scanner to initialize a group
for beacon in scanners[0].beacons[0]:
    scanners[0].offset = (0,0,0)
    beacons_aligned.append(beacon)

total_scanners = len(scanners) - 1
print(f"Total scanners to be aligned: {total_scanners}")
while any([scanner.offset is None for scanner in scanners]):
    aligned_fingerprints = generate_fingerprints(beacons_aligned)
    offset = -1
    for id, scanner in enumerate(scanners):
        if scanner.offset != None: #scanner has been aligned -> skip
            continue
        if len(scanner.finger_prints & aligned_fingerprints) < 12: #not matching scanner -> skip
            continue
        for index, rotated_beacons in scanner.beacons.items():
            for coord in rotated_beacons:
                #check every coord from current rotation and try to align it to already aligned beacons
                offset, beacons_offset = check_offset(coord, rotated_beacons)
                if offset != -1: #match found
                    scanner.offset = offset #save offset - for part2 and to skip scanner for further calculations
                    total_scanners -= 1
                    print(f"Scanner {id} aligned with an offset of {offset}, remaining scanners: {total_scanners}")
                    beacons_aligned = list(set(beacons_aligned) | beacons_offset)
                    break
            if offset != -1:
                break

print("Part 1:", len(beacons_aligned))

distances = list()
for i in range(len(scanners)-1):
    for j in range(i+1, len(scanners)):
        distances.append(manh_distance(scanners[i].offset, scanners[j].offset))

print("Part 2:", max(distances))
print(f"Total runtime: {datetime.now() - time_start}")
#total runtime for my data 1min:45sec