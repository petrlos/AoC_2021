#Advent of Code 2021: Day 21
def roll(player, cube):
    roll = (cube + 1) * 3
    player[0] += roll
    while player[0] > 10:
        player[0] -=10
    player[1] += player[0]
    return player

#MAIN
player1 = [4, 0] #position, score
player2 = [8, 0]

cube = 1

end = False
while not end:
    player1 = roll(player1, cube)
    cube += 3
    if player1[1] >= 1000:
        break
    player2 = roll(player2, cube)
    cube += 3
    if player2[1] >= 1000:
        break

print("Result task 1:")
print("[player 1 position, score], [player2 position, score], dice roll counter")
print(player1, player2, cube-1)

#from two scores select the smaller one, multiply by cube counter
#cube beginns with 1 -> subtract 1
result = min(list(zip(player1, player2))[-1])*(cube - 1)
print("Task 1:", result)