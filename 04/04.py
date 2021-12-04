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
    #checkRows
    for row in board:
        if len(set(row)) == 1:
            return True
    boardRotated = list(zip(*board[::-1]))
    for column in boardRotated:
        if len(set(column)) == 1:
            print("got you", column)
            return True
    return False

#MAIN
#first row only
numbers = [int(x) for x in lines[0].split(",")]

#third row and more
boardIndex, index = 0, 0
newBoard, boards = [], []
for line in lines[1:]:
    newBoard.append([int(x) for x in regNum.findall(line)])
    index +=1
    if index == 6:
        boards.append(newBoard[1:]) #ignore first row - empty
        newBoard = []
        index = 0

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
result = 0
for row in boards[winningBoardIndex]:
    result += sum(filter(None, row))

#Task1 - product last drawn number and sum of remaining numbers
print("Task 1:",result*drawnNumber)