#Advent of Code 2021: Day 18
import json
import re

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


    return -1

def split(sfn):
    sfn = str(sfn)
    numbers = list(map(int,(re.findall(r"\d+",sfn))))
    for num in numbers:
        if num >= 10:
            left, right = num//2, num//2 + num%2

            sfn = sfn.replace(str(num), f"[{left},{right}]", 1)
            break
    return json.loads(sfn)

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
            if splitted != result: #if splitted
                result = splitted
            else:
                reduced = True #not exploded and not splitted - number reduced

print(result)