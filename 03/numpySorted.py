import numpy
from random import randint

numpyArray = numpy.zeros((5,5), int)

for row in range(5):
    for column in range(5):
        numpyArray[(row, column)] = randint(0,2)

print(numpyArray)

sortedArray = numpyArray[numpyArray[:, 2].argsort()]
print(sortedArray)