#Advent of Code 2021: Day 18
import json
import re
from icecream import ic
from itertools import combinations

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

def split(sfn):
    sfn = str(sfn)
    numbers = list(map(int,(re.findall(r"\d+",sfn))))
    for num in numbers:
        if num >= 10:
            left, right = num//2, num//2 + num%2
            sfn = sfn.replace(str(num), f"[{left},{right}]", 1)
            break
    return json.loads(sfn)

def flatten(number, depth, path):
    #first call of this recursive
    results = []
    for i, item  in enumerate(number):
        if isinstance(item, list):
            results.extend(flatten(item, depth+1, path+[i]))
        else:
            results.append((item, depth, path + [i]))
    return results

def set_numb_with_path(nested_list, path, value):
    current = nested_list
    for index in path[:-1]:
        current = current[index]
    current[path[-1]] = value

def explode(number, flattened_numb):
    for id, numb in enumerate(flattened_numb):
        num, depth, path = numb
        if depth >=4:
            if id > 0: #if not the first, add to the left
                number_left, _, path_left = flattened_numb[id-1]
                set_numb_with_path(number, path_left, number_left+num)
            if id < len (flattened_numb)-2: #if not the last, add to the right
                number_right, _, path_right = flattened_numb[id+2]
                set_numb_with_path(number, path_right, number_right+flattened_numb[id+1][0])
            set_numb_with_path(number, path[:-1], 0) #set the pair to zero
            break #as soon as depth >= 4 is found
    return number

def sum_up_all_numbers(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = add_snailfish_numbers(result, number)  # add new number to existing one
        reduced = False
        while not reduced:
            flattened = flatten(result, 0, [])
            max_depht = max([depht[1] for depht in flattened])
            if max_depht >=4:
                result = explode(result, flattened)
            else:  # not exploded - try split
                splitted = split(result)
                if splitted != result:  # if splitted
                    result = splitted
                else:
                    reduced = True  # not exploded and not splitted - number reduced
    return result

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

numbers = [json.loads(json_string) for json_string in lines]

sum_up = sum_up_all_numbers(numbers)
print("Part 1:", count_magnitude(sum_up))