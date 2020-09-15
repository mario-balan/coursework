# -*- coding: utf-8 -*-

# Write two Python functions to find the minimum number in a list:
# - the first should be exponential O(n**2);
# - the second function should be linear O(n).

from random import randrange
from time import time

def findMinExponential(numList):
    min = numList[0]
    for i in numList:
        isMin = True
        for j in numList:
            if j < i:
                isMin = False
        if isMin:
            min = i
    return min

def findMinLinear(numList):
    min = numList[0]
    for i in numList:
        if i < min:
            min = i
    return min

powers = [0,1,2,3,4]

print("Linear:")
for listSize in [ 10**x for x in powers ]:
    list = [ randrange(10000) for x in range(listSize) ]
    startTime = time()
    findMinLinear(list)
    endTime = time()
    print("listSize:", listSize, "Time: ", endTime-startTime)

print("Exponential:")
for listSize in [ 10**x for x in powers ]:
    list = [ randrange(1000) for x in range(listSize) ]
    startTime = time()
    findMinExponential(list)
    endTime = time()
    print("listSize:", listSize, "Time: ", endTime-startTime)
