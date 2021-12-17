#Advent of Code 2021: Day 17
from datetime import datetime
start = datetime.now()

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def targetReached(coords):
    x, y = coords
    if x >= xLeft and x <= xRight:
        if y <= yTop and y >= yBottom:
            return True
    return False

def flyMore(coords):
    x, y = coords
    if x < xRight and y > yBottom:
        return True
    return False

def correctVelocity(velocity):
    x, y = velocity
    if x > 0:
        x -= 1
    elif x < 0:
        x += 1
    y -= 1
    return (x,y)

def throwWithVelocity(speedX, speedY):
    location = (0, 0)
    velocity = (speedX, speedY)
    topHeight = 0
    while flyMore(location):
        if location[1] > topHeight:
            topHeight = location[1]
        location = tupleSum(location, velocity)
        velocity = correctVelocity(velocity)
        if targetReached(location):
            return topHeight
    return None

#MAIN
import re
regNum = re.compile(r"-?\d+")
with open("data.txt") as file:
    input = file.read()
xLeft, xRight, yBottom, yTop = [int(x) for x in regNum.findall(input)]

topHeights = []
#ranges for initial speed has been set with brute force :)
for speedX in range(0, 350):
    for speedY in range(-100, 100):
        topHeight = throwWithVelocity(speedX, speedY)
        if topHeight != None:
            topHeights.append(topHeight)

print("Task 1:",max(topHeights))
print("Task 2:",len(topHeights))
print(datetime.now() - start)