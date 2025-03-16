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


#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

numbers = [json.loads(json_string) for json_string in lines]

for number in numbers:
    print(count_magnitude(number))
