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
    return -1

def split(number):
    return -1

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

numbers = [json.loads(json_string) for json_string in lines]

result = numbers[0]
for number in numbers[1:]:
    result = add_snailfish_numbers(result, number) #add new number to existing one
    new_number = result
    reduced = False
    while not reduced:
        explosive = True
        changed = False
        while explosive: #explsive loop - repeat until explosion possible
            new_number = explode(result)
            if new_number == -1: #not explosive anymore
                explosive = False
            else: #number exploded
                result = new_number
                changed = True

        splittable = True
        while splittable: #split loop
            new_number = split(result)
            if new_number == -1: #not splittable anymore
                splittable = False
            else: #number splitted
                result = new_number
                changed = True

        if not changed: #nothing happened in booths inner loops - leave outer loop
            reduced = True

print(result)