__author__ = 'Kalyan'

profiling_timing = '''
This involves adding sufficient time.perf_counter calls at appropriate places and then calculating difference to calculate
elapsed time.

https://docs.python.org/3/library/time.html#time.perf_counter

This is similar to print debugging, but once you have narrowed down code to a small code section by other means,
this can be very useful and precise.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit7_conversion_methods.py using time.clock() in this assignment.

for each value of count, execute the method 5 times and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

 Why 5 times and not just once? To get more data and to avoid the effects of noise (the outliers) due to so many things happening 
 on the system (like module imports, garbage collector running etc).
 
 Note: This is a python script which can be run from command line (python.exe <script>.py) or from pycharm (Right click -> Run <script>
 and not the usual pytest tests we have been using so far.
'''

import time
from unit8_conversion_methods import *
#print(*(list(locals().keys())),sep='\n')
#print(li)
# write clean code to run all the profiles in one go using loops, lists etc. Note that functions are first class objects
# in python so you can hold them in a list.
def profile_perf_counter():
    list1 = list(globals().keys())
    li = [j for j in list1 if j.count("num") + j.count("_string") == 2]
    li1 = iter(li)
    count = 10
    while True:
        try:
            item = li1.__next__()
            item1 = globals().get(item)
            for j in range(4):
                i = count ** (j + 1)
                times = []
                for _ in range(5):
                    before = time.clock()
                    item1(i)
                    after = time.clock()
                    times.append(after - before)
                timess = ["%.6f" % k for k in times]
                #timess = [k[1:-1] for k in timers]
                min1 = min(timess)
                st = "{0}, count = {1}, min = {2}, actuals = [{3}]".format(item, i, min1, ", ".join(timess))
                print(st)
        except StopIteration:
            break


# write your findings on what is the most optimal method and what you learnt in the process.
summary = '''


'''

if __name__ == "__main__":
    profile_perf_counter()
