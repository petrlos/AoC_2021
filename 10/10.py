#Advent of Code 2021: Day 10
from datetime import datetime
start = datetime.now()

with open("data.txt") as file:
    lines = file.read().splitlines()

#task1 score table - first corrupted chunk becomes that score
scoreTable = {")":3, "]":57, "}": 1197, ">": 25137}
#task2 score table
scoreMultiplier = {")":1, "]":2, "}":3, ">":4}

chunkOpen = "([{<"
chunkClose = {")":"(", "]":"[", "}":"{", ">":"<"} #needed for task1
chunkFinish = {"(":")", "[":"]", "{":"}", "<":">"} #needed for task2

scoreTask1 = 0
scoreTask2 = []
for line in lines:
    chunkChecker = ""
    lineCorrupted = False
    for chunk in line:
        if chunk in chunkOpen: #chunk opens - add to chunkchecker
            chunkChecker += chunk
        if chunk in chunkClose: #chunk closes - must be the same as the last opened chunk
            if chunkChecker[-1] == chunkClose[chunk]:
                chunkChecker = chunkChecker[:-1] #can be closed - close
            else:
                scoreTask1 += scoreTable[chunk] #cannot be closed: line is corrupted
                lineCorrupted = True
        if lineCorrupted: #dont check other chunks if line corrupted
            break
    if not lineCorrupted: #task2
        lineScore = 0
        closingSequence = ""
        for char in reversed(chunkChecker): #generate reversed sequence to close up
            closingSequence += chunkFinish[char]
        for char in closingSequence: #count line score
            lineScore *= 5
            lineScore += scoreMultiplier[char]
        scoreTask2.append(lineScore)

print("Task 1:",scoreTask1)
print("Task 2:",sorted(scoreTask2)[len(scoreTask2) // 2]) #result is middle value
print("Runtime:", datetime.now() - start)