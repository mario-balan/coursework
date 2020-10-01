# -*- coding: utf-8 -*-

# measuring the time for different methods of list generation:

from timeit import Timer

def concatenate():
    l = []
    for i in range(1000):
        l = l + [i]

def append():
    l = []
    for i in range(1000):
        l.append(i)

def listComprehension():
    l = [i for i in range(1000)]

def listRange():
    l = list(range(1000))

def empty():
    pass


# the imports below are intended to execute function in the timeit environment.
# the times reported include the time spent in function calling.

print("Timings including function calls:")
t1 = Timer("concatenate()", "from __main__ import concatenate")
print("Concatenate: ",t1.timeit(number=1000), "milliseconds.")
t2 = Timer("append()", "from __main__ import append")
print("Append: ",t2.timeit(number=1000), "milliseconds.")
t3 = Timer("listComprehension()", "from __main__ import listComprehension")
print("listComprehension: ",t3.timeit(number=1000), "milliseconds.")
t4 = Timer("listRange()", "from __main__ import listRange")
print("listRange: ",t4.timeit(number=1000), "milliseconds.")

print("\nTimings excluding function calls:")
t5 = Timer("empty()", "from __main__ import empty")
empty = t5.timeit(number=1000)

t1 = Timer("concatenate()", "from __main__ import concatenate")
print("Concatenate: ",t1.timeit(number=1000) - empty, "milliseconds.")
t2 = Timer("append()", "from __main__ import append")
print("Append: ",t2.timeit(number=1000) - empty, "milliseconds.")
t3 = Timer("listComprehension()", "from __main__ import listComprehension")
print("listComprehension: ",t3.timeit(number=1000) - empty, "milliseconds.")
t4 = Timer("listRange()", "from __main__ import listRange")
print("listRange: ",t4.timeit(number=1000) - empty, "milliseconds.")

print("\nreference (time to run an empty function): ",empty, "milliseconds.")
