# -*- coding: utf-8 -*-

from logic_gates import *

class halfAdder(BinaryGate):
    '''A half adder is a combination of a XOR and an AND gate, but here it is implemented
    as a BinaryGate of its own (sum and carry will be passed as a list [sum, carry]).'''
    
    def __init__(self, n):
        super(halfAdder,self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a != b):
            return 1, 0
        elif (a == 0 and b == 0):
            return 0, 0
        else:
            return 1, 1

A = halfAdder('Adder')
print(A.performGateLogic())
