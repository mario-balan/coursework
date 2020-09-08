from logic_gates import *

def exampleOne():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)

    c1.printConnection()
    c2.printConnection()
    c3.printConnection()

    print(g4.getOutput())

def challengeOne():
    g1 = NandGate("G1")
    g2 = NandGate("G2")
    g3 = AndGate("G3")

    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)

    print(g3.getOutput())

def main():
    resultOne = exampleOne()
    resultTwo = challengeOne()
    print(resultOne == resultTwo)

main()
