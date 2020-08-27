import random

def generate_one(strlen):
    alphabet = "abcdefghijklmnopqrstuvxz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(len(alphabet))]
    return res

def score(goal, teststring):
    num_same = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            num_same = num_same + 1
    return num_same / len(goal)


def main():

    goalstring = "methinks it is like a weasel"
    newstring = generate_one(len(goalstring))
    best = 0
    newscore = score(goalstring,newstring)

    while newscore < 1:
        if newscore > best:
            print(newscore,newstring)
            best = newscore
        newstring = generate_one(len(goalstring))
        newscore = score(goalstring,newstring)

main()
