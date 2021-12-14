from functools import reduce

numbers = [int(x) for x in "65 ^ 9 ^ 27 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22".split(" ^ ")]

print(reduce(lambda x, y: x ^ y, numbers))

