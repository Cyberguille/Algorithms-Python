__author__ = 'Ramon'


def get_input(filename):
    array = []

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        array.append(values.pop(0))

    return array


def sum2(array, T):
    counter = 0
    mem = list()
    for t in T:
        for x in array:
            if not x in mem:
                mem.append(x)
                if (t-x) in array and (t-x != x):
                    print(t-x, '+', x, '=', t)
                    counter += 1
                    break
        mem.clear()

    return counter

array = [1, 1, 2, 3, 4, 6, 8]
H = list()

for i in range(0, 20):
    H.append(i)

print(sum2(array, H))
#-----------------------------------------------------------------------------------


def f(v, i, S, memo):
    if i >= len(v): return 1 if S == 0 else 0
    if (i, S) not in memo:  # <-- Check if value has not been calculated.
        count = f(v, i + 1, S, memo)
        count += f(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count  # <-- Memoize calculated result.
    return memo[(i, S)]     # <-- Return memorized value.

v = [4, 3, 2, 1]
sum = 5
memo = dict()
#print(f(v, 0, sum, memo))
#-----------------------------------------------------------------------------------

import bisect


def two_sum(array):
    """Returns the numbers from [-WIDTH, WIDTH] that can be obtained by
    summing up any two elements in 'array'."""

    WIDTH = 10000
    out = set()
    for i in array:
        lower = bisect.bisect_left(array, -WIDTH - i)
        upper = bisect.bisect_right(array, WIDTH - i)
        out |= set([i + j for j in array[lower:upper]])
    return out

