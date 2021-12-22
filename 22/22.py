#Advent of Code 2021: Day 22
import re
def performLineIn5050(onOff, numbers): #on = True, off = False
    for index, number in enumerate(numbers): #set borders for Task1
        if number not in range(-50, 51):
            if number > 50:
                numbers[index] = 50
            elif number < -50:
                numbers[index] = -50
    x1, x2, y1, y2, z1, z2 = numbers
    if not (x1 == x2 or y1 == y2 or z1 == z2): #checkBorders
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    cube = (x, y, z)
                    if onOff:
                        cubes.add((x,y,z))
                    else:
                        try:
                            cubes.remove(cube)
                        except:
                            ...

#MAIN
regNum = re.compile(r"-?\d+")
with open("test2.txt") as file:
    lines = file.read().splitlines()

cubes = set()
for line in lines:
    if "on" in line:
        performLineIn5050(True, [int(x) for x in regNum.findall(line)])
    elif "off" in line:
        performLineIn5050(False, [int(x) for x in regNum.findall(line)])
    else:
        print("no valid instruction")
print("Task 1:",len(cubes))