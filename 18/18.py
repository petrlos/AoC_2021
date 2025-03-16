#Advent of Code 2021: Day 18
import json

def count_magnitude(number):
    result = 0
    left, right = number
    if isinstance(left, list):
        result += 3* count_magnitude(left)
    if isinstance(right, list):
        result += 2* count_magnitude(right)
    if isinstance(left, int):
        result += 3 * left
    if isinstance(right, int):
        result += 2* right
    return result

def add_snailfish_numbers(num1, num2):
    return [num1, num2]

def explode(number):
    if number == [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]:
        return [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
    if number == [[[[0,7],4],[7,[[8,4],9]]],[1,1]]:
        return [[[[0,7],4],[15,[0,13]]],[1,1]]

    return -1

def split(number):
    if number == [[[[0,7],4],[15,[0,13]]],[1,1]]:
        return [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    return -1

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

numbers = [json.loads(json_string) for json_string in lines]

result = numbers[0]
for number in numbers[1:]:
    result = add_snailfish_numbers(result, number) #add new number to existing one
    reduced = False
    while not reduced:
        exploded = explode(result) #try explode
        if exploded != -1:  #if exploded
            result = exploded
        else: #not exploded - try split
            splitted = split(result)
            if splitted != -1: #if splitted
                result = splitted
            else:
                reduced = True #not exploded and not splitted - number reduced

print(result)