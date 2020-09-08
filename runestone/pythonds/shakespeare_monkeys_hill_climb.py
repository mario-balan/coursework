# -*- coding: utf-8 -*-

import random

def generate_one(strlen,alphabet):
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(len(alphabet))]
    return res

def generate_climb(strlen,beststring,goalstring,alphabet):
    res = ""
    for i in range(strlen):
        if beststring[i] == goalstring[i]:
            res = res + beststring[i]
        else:
            res = res + alphabet[random.randrange(len(alphabet))]
    return res

def score(goal,teststring):
    num_same = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            num_same = num_same + 1
    return num_same / len(goal)


def main():

    goalstring = "tomorrow, and tomorrow, and tomorrow,\n\
creeps in this petty pace from day to day,\n\
to the last syllable of recorded time;\n\
and all our yesterdays have lighted fools\n\
the way to dusty death. out, out, brief candle!\n\
life's but a walking shadow, a poor player\n\
that struts and frets his hour upon the stage,\n\
and then is heard no more. it is a tale\n\
told by an idiot, full of sound and fury,\n\
signifying nothing."

    alphabet = "abcdefghijklmnopqrstuvwxyz /,.;'!\n"
    newstring = generate_one(len(goalstring),alphabet)
    best = 0
    newscore = score(goalstring,newstring)
    count = 0
    n = 0

    while newscore < 1:
        count+=1
        if newscore > best:
            if n == 10: # imprime de 10 em 10 (uma brincadeira posterior)
                print("\n",newscore,"\n"+newstring)
                n = 0
            else:
                n += 1
            best = newscore
        newstring = generate_climb(len(goalstring),newstring,goalstring,alphabet)
        newscore = score(goalstring,newstring)

    print("\n",newscore,"\n"+newstring)
    print("\nNumber of cicles: %d" % count)

main()
