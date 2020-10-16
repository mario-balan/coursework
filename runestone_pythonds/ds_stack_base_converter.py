# -*- coding: utf-8 -*-

from data_structures import Stack

def baseConverter(decNum,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNum > 0:
        remainder = decNum % base
        remstack.push(remainder)
        decNum = decNum // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(256,2))
print(baseConverter(256,8))
print(baseConverter(256,16))
print(baseConverter(26,26))
