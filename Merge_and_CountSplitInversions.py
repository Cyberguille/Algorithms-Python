__author__ = 'Ramon'

import timeit


def merge_countSplitInv(B, C):
    i, j, count = 0, 0, 0
    D = []
    #print(B, C)
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            count += len(B[i:])

    D += B[i:]
    D += C[j:]

    return D, count


def merge_count(A):
    if len(A) == 1:
        return A, 0
    else:
        B, x = merge_count(A[:int(len(A)/2)])
        C, y = merge_count(A[int(len(A)/2):])
        D, z = merge_countSplitInv(B, C)
        return D, (x + y + z)


def main1():
    #A = [8, 7, 6, 5, 4, 3, 2, 1]
    A = list(range(0, 10001, 1))
    A.reverse()
    sorted_array, inversions = merge_count(A)
    #print("Sorted Array:" + str(sorted_array) + " with " + str(inversions) + " inversions")
    #print("Probando picar el array A")
    #n = int(len(A)/2)
    #print("A[:n]=", A[:n])
    #print("A[n:]=

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main1()', setup='from __main__ import main1', number=1)
print('total time 1=', result*1000, 'ms')


def main2():
    A = list(range(0, 1001, 1))
    A.reverse()
    sorted_array, inversions = merge_count(A)

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main2()', setup='from __main__ import main2', number=1)
print('total time 2=', result*1000, 'ms')


def main3():
    A = [8, 7, 6, 5, 4, 3, 2, 1]
    sorted_array, inversions = merge_count(A)

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main3()', setup='from __main__ import main3', number=1)
print('total time 3=', result*1000, 'ms')