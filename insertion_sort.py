__author__ = 'Ramon'

import timeit


def main():
    #  A = [8, 7, 6, 5, 4, 3, 2, 1]
    #  print(A)
    A = list(range(0, 1001, 1))
    A.reverse()

    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

    #print(A)


def main2():
    A = list(range(0, 1001, 1))
    A.reverse()
    A.sort()

result = timeit.timeit('main()', setup='from __main__ import main', number=1)
result2 = timeit.timeit('main2()', setup='from __main__ import main2', number=1)
print('total main time=', result*1000, 'ms')
print('total main2 time=', result2*1000, 'ms')
