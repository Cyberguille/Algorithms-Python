__author__ = 'Ramon'

import timeit
import BinarySearchTree as BST


def get_input(filename):
    array = []

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        array.append(values.pop(0))

    return array


def sum2(array, T):
    counter = 0

    for t in T:
        for x in array:
            if (t-x) in array and (t-x != x):
                #print(t-x, '+', x, '=', t)
                counter += 1
                break

    return counter


def sum2Hash(array, T):
    counter = 0
    H = dict()

    for i in range(0, len(array)):
        H[array[i]] = array[i]

    #print(array)
    #print(H)

    for t in T:
        for x in array:
            if (t-x) in H and (t-x != x):
                #print(t-x, '+', x, '=', t)
                counter += 1
                break

    return counter


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)


def sum2b(array, T):
    counter = 0

    for t in T:
        for x in array:
            if binarySearchRecursive(array, t-x) and (t-x != x):
                #print(t-x, '+', x, '=', t)
                counter += 1
                break

    return counter


def create_list_consecutive_numbers(width):
    T = list()

    for i in range(-width, width+1):
        T.append(i)

    return T


def test1():
    T = create_list_consecutive_numbers(10000)
    array1 = [1, 1, 2, 3, 4, 6, 8]  # test Answer = 11
    array1a = [8, 1, 4, 3, 6, 2, 1]  # test Answer = 11
    print(sum2(array1a, T))


def test1b():
    T = create_list_consecutive_numbers(10000)
    array1 = [1, 1, 2, 3, 4, 6, 8]  # test Answer = 11
    array1a = [8, 1, 4, 3, 6, 2, 1]  # test Answer = 11
    array1a.sort()
    print(sum2b(array1a, T))


def test2():
    T = create_list_consecutive_numbers(10000)
    array2 = [-10001, 1, 2, -10001]     # test Answer = 3
    print(sum2(array2, T))


def test2a():
    T = create_list_consecutive_numbers(10000)
    array2 = [-10001, 1, 2, -10001]     # test Answer = 3
    array2.sort()
    print(sum2(array2, T))


def test3():
    T = create_list_consecutive_numbers(10000)
    array3 = [-10001, 1, 2, -10001, 9999]     # test Answer = 5
    print(sum2(array3, T))


def main():
    T = create_list_consecutive_numbers(10000)
    array = get_input("2sumtest1.txt")
    #array.sort()
    print(sum2Hash(array, T))


def sum2_bst(bst, T, array):
    counter = 0

    for t in T:
        for x in array:
            if bst.search(t-x) is not None and (t-x != x):
                #print(t-x, '+', x, '=', t)
                counter += 1
                break

    return counter


def bst_main():
    T = create_list_consecutive_numbers(10000)
    array = get_input("2sumtest1.txt")
    bst = BST.BinarySearchTree(array)
    print(sum2_bst(bst, T, array))

# result is the time (in seconds) to run the whole loop
#result = timeit.timeit('bst_main()', setup='from __main__ import bst_main', number=1)
#print('total time bst_main=', result*1000, 'ms')

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main()', setup='from __main__ import main', number=1)
print('total time main=', result*1000, 'ms')

# result is the time (in seconds) to run the whole loop
#result = timeit.timeit('test2()', setup='from __main__ import test2', number=1)
#print('total time test2 =', result*1000, 'ms')
# result is the time (in seconds) to run the whole loop
#result = timeit.timeit('test2a()', setup='from __main__ import test2a', number=1)
#print('total time test2a =', result*1000, 'ms')

# result is the time (in seconds) to run the whole loop
#result = timeit.timeit('test1()', setup='from __main__ import test1', number=1)
#print('total time test1=', result*1000, 'ms')
# result is the time (in seconds) to run the whole loop
#result = timeit.timeit('test1b()', setup='from __main__ import test1b', number=1)
#print('total time test1b=', result*1000, 'ms')