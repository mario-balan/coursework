# -*- coding: utf-8 -*-

from logic_gates import *

class halfAdder(BinaryGate):
    '''A half adder is a combination of a XOR and an AND gate, but here it is implemented
    as a BinaryGate of its own (sum and carry will be passed as a list [carry, sum]).'''

    def __init__(self, n):
        super(halfAdder,self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a != b):
            return 0, 1
        elif (a == 0 and b == 0):
            return 0, 0
        else:
            return 1, 1

class fullAdder(halfAdder):
    def __init__(self, n):
        super(fullAdder,self).__init__(n)
        self.pinC = None

    def getPinC(self):
        if self.pinC == None:
            return int(input("Enter Pin C input for gate " + self.getLabel()+"-->"))
        else:
            return self.pinC.getFrom().getOutput()

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        c = self.getPinC()

        sum = 1 if ((a != b) != c) else 0
        carry = 1 if ((a and b) or (a and c) or (b and c)) else 0

        return carry, sum

H = halfAdder('Half')
#print(H.performGateLogic())

F = fullAdder('Full')
print(F.performGateLogic())
