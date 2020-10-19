# -*- coding: utf-8 -*-

from data_structures import Deque

def palindromeChecker(string):
    chardeque = Deque()

    for ch in string:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palindromeChecker("lsdkjfskf"))
print(palindromeChecker("radar"))
print(palindromeChecker("merecerem"))
