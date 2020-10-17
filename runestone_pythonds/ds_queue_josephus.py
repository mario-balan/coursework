# -*- coding: utf-8 -*-

from data_structures import Queue

def josephusProblem(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(josephusProblem(["Zazá","Mário","Guilherme","Lila","Sumiço","Mayara"],7))
