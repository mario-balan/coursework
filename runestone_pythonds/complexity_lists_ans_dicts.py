# -*- coding: utf-8 -*-

from timeit import Timer

def empty():
    pass

t0 = Timer("empty()", "from __main__ import empty")
empty = t0.timeit(number=1000)

# the list .index() operator is 𝑂(n):
print("1- the list .index() operator is 𝑂(n):")

def getListIndex(element):
    return list.index(element)

listSize = (10 ** 5) + 1
list = [ x for x in range(listSize) ]

i = 1
while i < len(list):
    t1 = Timer("getListIndex(%d)" %i, "from __main__ import getListIndex")
    print("LIST: .index(%d)" %i, "retrieved in", t1.timeit(number=1000) - empty)
    i *= 10

# to retrieve an element from a list by the index is 𝑂(1):
print("\n2- to retrieve an element from a list by the index is 𝑂(1):")

def getByListIndex(index):
    return list[index]

i = 1
while i < len(list):
    t2 = Timer("getByListIndex(%d)" %i, "from __main__ import getByListIndex")
    print("LIST: list[%d])" %i, "retrieved in", t2.timeit(number=1000) - empty)
    i *= 10

# get item and set item are 𝑂(1) for dictionaries:
print("\n3- get item and set item are 𝑂(1) for dictionaries:")

def setDictItem(key, value):
    dict[key] = value

def getDictItem(key):
    return dict.get(key)


dictSize = (10 ** 5) + 1
dict = {key: value for (key, value) in zip(range(dictSize),range(dictSize))}

i = 1
while i < len(dict):
    t1 = Timer("setDictItem(%d, %d)" %(i,i), "from __main__ import setDictItem")
    print("DICT: .set(%d,%d)"%(i,i),"in", t1.timeit(number=1000) - empty)
    i *= 10

i = 1
while i < len(dict):
    t2 = Timer("getDictItem(%d)" %i, "from __main__ import getDictItem")
    print("DICT: .get(%d)"%i,"in", t2.timeit(number=1000) - empty)
    i *= 10

# comparing del times in lists and dictionaries (both are 𝑂(1)):
print("\n4- comparing deletion times in lists and dictionaries (both are 𝑂(1)):")

def listDel(index):
    del list[index]

def dictDel(key):
    del dict[key]


i = 1
t1 = Timer("listDel(%d)" %i, "from __main__ import listDel")
t2 = Timer("dictDel(%d)" %i, "from __main__ import dictDel")

while i < len(dict):
    t1 = Timer("listDel(%d)" %i, "from __main__ import listDel")
    t2 = Timer("dictDel(%d)" %i, "from __main__ import dictDel")
    tList = t1.timeit(number=1)
    tDict = t2.timeit(number=1)
    print("LIST: .del(%d)"%i,"in", tList)
    print("DICT: .del(%d)"%i,"in", tDict)
    print(("List" if tList < tDict else "Dictionary"),"is faster. The difference is", abs(tDict - tList),"\n")
    i *= 10
