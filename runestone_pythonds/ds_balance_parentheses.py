# -*- coding: utf-8 -*-

from data_structures import Stack
import sys

def parChecker(string):
    s = Stack()
    i = 0
    balanced = True

    while i < len(string) and balanced:
        symbol = string[i]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            elif symbol == ")":
                    s.pop()
        i += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

try:
    print(parChecker(sys.argv[1])) # input a string:
except:
    print("You must pass a string with some parentheses as the argument.")
