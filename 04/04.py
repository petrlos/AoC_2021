#Advent of Code 2021: Day 4
import re
regNum = re.compile(r"\d+")

with open("data.txt") as file:
    lines = file.read().splitlines()

def markNumber(board, drawnNumber):
    for rowIndex, row in enumerate(board):
        for columnIndex, number in enumerate(row):
            if number == drawnNumber:
                board[rowIndex][columnIndex] = None

def boardCompleted(board):
    for row in board:
        if len(set(row)) == 1:
            return True
    boardRotated = list(zip(*board[::-1]))
    for column in boardRotated:
        if len(set(column)) == 1:
            return True
    return False

def createBoard(lines):
    # third row and more
    boardIndex, index = 0, 0
    newBoard, boards = [], []
    for line in lines[1:]:
        newBoard.append([int(x) for x in regNum.findall(line)])
        index += 1
        if index == 6:
            boards.append(newBoard[1:])  # ignore first row - empty
            newBoard = []
            index = 0
    return boards

def remainingNumbersSum(board):
    result = 0
    for row in board:
        result += sum(filter(None, row))
    return result

#MAIN
#first row only
numbers = [int(x) for x in lines[0].split(",")]

"""#Task1
boards = createBoard(lines)
weHaveAWinner = False
numberIndex = 0
while not weHaveAWinner:
    drawnNumber = numbers[numberIndex]
    for boardIndex, board in enumerate(boards):
        markNumber(board, drawnNumber)
        boardComplete = boardCompleted(board)
        if boardComplete:
            weHaveAWinner = True
            winningBoardIndex = boardIndex
    numberIndex += 1
#get sum of remaining numbers:
sumOfRemainingNumbers = remainingNumbersSum(boards[winningBoardIndex])
print("Task 1:",sumOfRemainingNumbers*drawnNumber)"""

#Task1 + 2
boards = createBoard(lines)
results = []
for number in numbers:
    boardComplete = False
    for boardIndex, board in enumerate(boards):
        if board != None:
            markNumber(board, number)
            boardComplete = boardCompleted(board) #check if board completed
        if boardComplete:
            numbersSum = remainingNumbersSum(boards[boardIndex])
            results.append(numbersSum * number)
            boards[boardIndex] = None
    boards = list(filter(lambda x: x != None, boards))

print("Task 1:", results[0])
print("Task 2:", results[-1])