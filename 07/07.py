#Advent of Code 2021 Day 7
from datetime import datetime
start = datetime.now()

with open("data.txt") as file:
    crabShips = [int(x) for x in file.read().split(",")]

fuelCosts = []
for possibleDepth in range(max(crabShips) + 1):
    fuelCosts.append(sum(range(possibleDepth+1)))

resultsTask1 = []
resultsTask2 = []
for depth in range(0, max(crabShips)):
    checkSumTask1 = 0
    checkSumTask2 = 0
    for crabShip in crabShips:
        checkSumTask1 += abs(depth - crabShip)
        # FIRST SOLUTION: 24 sek runtime: checkSumTask2 += sum(range(abs(number - depth)+1))
        checkSumTask2 += fuelCosts[abs(depth - crabShip)]
    resultsTask1.append(checkSumTask1)
    resultsTask2.append(checkSumTask2)

print("Task 1:",min(resultsTask1))
print("Task 2:",min(resultsTask2))
print("Runtime: ", datetime.now() - start)