# -*- coding: utf-8 -*-

# three different algorithms to achieve the same goal:
# check if two words are anagrams

from timeit import Timer
import random, string


def anagramCheckOff(w1, w2):
    stillPossible = True
    if len(w1) != len(w2):
        stillPossible = False

    w2List = list(w2) # because strings can't be altered.
    pos1 = 0

    while pos1 < len(w1) and stillPossible:
        pos2 = 0
        found = False
        while pos2 < len(w2List) and not found:
            if w1[pos1] == w2List[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            w2List[pos2] = None
        else:
            stillPossible = False

        pos1 = pos1 + 1

    return stillPossible

def anagramSortCompare(w1,w2):
    w1List = list(w1)
    w2List = list(w2)

    w1List.sort()
    w2List.sort()

    pos = 0
    matches = True

    while pos < len(w1) and matches:
        if w1List[pos]==w2List[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


def anagramCountCompare(w1,w2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(w1)):
        pos = ord(w1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(w2)):
        pos = ord(w2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillPossible = True
    while j<26 and stillPossible:
        if c1[j]==c2[j]:
            j += 1
        else:
            stillPossible = False

    return stillPossible


strLength = 10000

word1 = "".join(random.choice(string.ascii_lowercase) for _ in range(strLength))
word2 = "".join(random.sample(word1, len(word1)))
word3 = "".join(random.choice(string.ascii_lowercase) for _ in range(strLength))
print("First String =", word1)
print("Second String =", word2)

#print(anagramCheckOff(word1,word2))
#print(anagramSortCompare(word1,word2))
#print(anagramCountCompare(word1,word2))

print("For two strings of size", strLength, "that ARE anagrams:")
t1 = Timer("anagramCheckOff('%s', '%s')" %(word1, word2), "from __main__ import anagramCheckOff")
print("Checking Off: ",t1.timeit(number=1), "milliseconds in 𝑂(𝑛2).")
t2 = Timer("anagramSortCompare('%s', '%s')" %(word1, word2), "from __main__ import anagramSortCompare")
print("Sort and Compare: ",t2.timeit(number=10), "milliseconds in 𝑂(𝑛log𝑛).")
t3 = Timer("anagramCountCompare('%s', '%s')" %(word1, word2), "from __main__ import anagramCountCompare")
print("Count and Compare: ",t3.timeit(number=10), "milliseconds in 𝑂(𝑛).")

print("For two strings of size", strLength, "that ARE NOT anagrams:")
t1 = Timer("anagramCheckOff('%s', '%s')" %(word1, word3), "from __main__ import anagramCheckOff")
print("Checking Off: ",t1.timeit(number=1), "milliseconds in 𝑂(𝑛2).")
t2 = Timer("anagramSortCompare('%s', '%s')" %(word1, word3), "from __main__ import anagramSortCompare")
print("Sort and Compare: ",t2.timeit(number=10), "milliseconds in 𝑂(𝑛log𝑛).")
t3 = Timer("anagramCountCompare('%s', '%s')" %(word1, word3), "from __main__ import anagramCountCompare")
print("Count and Compare: ",t3.timeit(number=10), "milliseconds in 𝑂(𝑛).")
