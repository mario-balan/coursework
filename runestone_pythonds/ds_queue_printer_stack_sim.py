# -*- coding: utf-8 -*-

import random
from data_structures import Queue

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask(students):
    chance = 3600 / (students * 2)
    num = random.randrange(1, chance + 1)
    if num == chance:
        return True
    else:
        return False

def simulation(numSeconds, numStudents, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask(numStudents):
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum (waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))
    return averageWait

allAverages = []

for i in range(10):
    allAverages.append(simulation(3600,20,10))

allAverages.sort()
print("\nSmallest Average Wait: %6.2f secs."%(allAverages[0]))
print("Largest Average Wait: %6.2f secs."%(allAverages[-1]))
print("Average Average Wait Time: %6.2f secs."%(sum(allAverages) / len(allAverages)))
