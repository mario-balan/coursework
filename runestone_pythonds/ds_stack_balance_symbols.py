# -*- coding: utf-8 -*-

from data_structures import Stack
import sys

def matches(open, close):
    openers = "([{"
    closers = ")]}"
    return openers.index(open) == closers.index(close)

def parChecker(string):
    s = Stack()
    i = 0
    balanced = True

    while i < len(string) and balanced:
        symbol = string[i]
        if symbol in "([{":
            s.push(symbol)
        elif s.isEmpty():
            balanced = False
        elif symbol in ")]}":
            top = s.pop()
            if not matches(top,symbol):
               balanced = False
        i += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

try:
    print(parChecker(sys.argv[1])) # input a string:
except:
    print("You must pass a string with some parentheses, brackets and curly braces as the argument.")
