__author__ = 'Ramon'

import timeit
import sys
import random

sys.setrecursionlimit(1500)


def partition(A, p, r):
    #print('A='+str(A))
    counter = 0
    x = A[r]
    i = p-1
    #print('x='+str(x))
    #print('i='+str(i))
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            #print('A[i]='+str(A[i])+' A[j]='+str(A[j]))
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    #print('A[i+1]='+str(A[i+1])+' A[r]='+str(A[r]))
    #print('i+1='+str(i+1))
    counter += i
    return i+1, counter


def QuickSort(A, p, r):
    if p < r:
        q, c = partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
        return A, c


def main():
    #array = [2, 3, 5, 7, 8, 1, 4, 6]
    array = list(range(0, 1001, 1))
    array.reverse()
    A, c = QuickSort(array, 0, len(array)-1)
    print(A)
    print(c)

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main()', setup='from __main__ import main', number=1)
print('total time=', result*1000, 'ms')

#******************************************************************************************
#RANDOM version


def randomized_partition(A, p, r):
    pivotIndex = random.randint(p, r)
    A[r], A[pivotIndex] = A[pivotIndex], A[r]
    return partition(A, p, r)


def randomized_QuickSort(A, p, r):
    if p < r:
        q, c = randomized_partition(A, p, r)
        randomized_QuickSort(A, p, q-1)
        randomized_QuickSort(A, q+1, r)
        return A, c


def main2():
    #array = [2, 3, 5, 7, 8, 1, 4, 6]
    array = list(range(0, 10001, 1))
    array.reverse()
    A, c = randomized_QuickSort(array, 0, len(array)-1)
    print(A)
    print(c)

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main2()', setup='from __main__ import main2', number=1)
print('total time2=', result*1000, 'ms')