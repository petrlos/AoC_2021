#Advent of Code 2021 Day 7
from datetime import datetime
start = datetime.now()

with open("data.txt") as file:
    numbers = [int(x) for x in file.read().split(",")]

resultsTask1 = []
resultsTask2 = []
for depth in range(1, max(numbers)):
    checkSumTask1 = 0
    checkSumTask2 = 0
    for number in numbers:
        checkSumTask1 += abs(depth - number)
        checkSumTask2 += sum(range(abs(number - depth)+1))
    resultsTask1.append(checkSumTask1)
    resultsTask2.append(checkSumTask2)

print("Task 1:",min(resultsTask1))
print("Task 2:",min(resultsTask2))
print("Runtime: ", datetime.now() - start)