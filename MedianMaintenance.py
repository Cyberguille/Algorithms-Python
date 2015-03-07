__author__ = 'Ramon'

import heap as h


def get_input(filename):
    array = []

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        array.append(values.pop(0))

    return array


def median(array):
    med = [array.pop(0)]
    # h_high[0] has the minimum values of the highest values
    h_high = h.Heap(list())
    # h_low[0] has the maximum value of the lowest values
    h_low = h.Heap(list(), True)

    h_low.insert(med[0])

    for i in array:
        # trying to keep both Heaps balanced
        if i < h_low[0]:
            h_low.insert(i)
        else:
            h_high.insert(i)
        if h_low.__sizeof__() > h_high.__sizeof__() + 1:
            h_high.insert(h_low.extract())
        elif h_low.__sizeof__() + 1 < h_high.__sizeof__():
            h_low.insert(h_high.extract())
        if h_low.__sizeof__() >= h_high.__sizeof__():
            med.append(h_low[0])
        else:
            med.append(h_high[0])

    return med

array = get_input('Median.txt')
print(sum(median(array)) % 10000)



