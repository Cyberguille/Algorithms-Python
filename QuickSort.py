__author__ = 'ramon'


#via 1
def qsort1(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return qsort1(less)+equal+qsort1(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array,
    # just return the array.
        return array


#via 2
def qsort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort2([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort2([x for x in arr[1:] if x >= arr[0]])


#via 3
def qsort3(items):
    if not len(items) > 1:
        return items
    items, pivot = partition(items)
    return qsort3(items[:pivot]) + [items[pivot]] + qsort3(items[pivot + 1:])


def partition(items):
    i = 1
    pivot = 0
    for j in range(1, len(items)):
        if items[j] <= items[pivot]:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i - 1], items[pivot] = items[pivot], items[i - 1]
    return items, i - 1


#probando
array = [12, 4, 5, 6, 7, 3, 1, 15]
#array = list(range(0, 1001, 1))
#array.reverse()
print(qsort3(array))