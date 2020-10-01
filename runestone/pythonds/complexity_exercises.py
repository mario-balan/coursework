# -*- coding: utf-8 -*-

from timeit import Timer

def empty():
    pass

t0 = Timer("empty()", "from __main__ import empty")
empty = t0.timeit(number=1000)

# the list index operator is 𝑂(1):

def getListIndex(element):
    return list.index(element)

listSize = (10 ** 6) + 1
list = [ x for x in range(listSize) ]

i = 1
t1 = Timer("getListIndex(%d)" %i, "from __main__ import getListIndex")

while i < len(list):
    print("LIST: .index(%d)" %i, "retrieved in", t1.timeit(number=1000) - empty)
    i *= 10

# get item and set item are 𝑂(1) for dictionaries:

def setDictItem(key, value):
    dict[key] = value

def getDictItem(key):
    return dict.get(key)


dictSize = (10 ** 5) + 1
dict = {key: value for (key, value) in zip(range(dictSize),range(dictSize))}

i = 1
t2 = Timer("setDictItem(%d, %d)" %(i,i), "from __main__ import setDictItem")
t3 = Timer("getDictItem(%d)" %i, "from __main__ import getDictItem")

while i < len(dict):
    print("DICT: .set(%d,%d)"%(i,i),"in", t2.timeit(number=1000) - empty)
    i *= 10

i = 1
while i < len(dict):
    print("DICT: .get(%d)"%i,"in", t3.timeit(number=1000) - empty)
    i *= 10
