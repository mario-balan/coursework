# -*- coding: utf-8 -*-

from timeit import Timer
from random import randrange


listSize = 10 ** 6

list = [ randrange(listSize) for x in range(listSize) ]

# Sort and get by index in 𝑂(𝑛log(𝑛)):

def findKthMin(k):
    return sorted(list)[k]

print(findKthMin(7))

# Trying to reduce complexity from 𝑂(𝑛log(𝑛)):
# I read about using MinHeaps and Quicksort.
# For now I'll leave it aside and come back
#   after I cover these topics.
