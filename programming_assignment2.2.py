__author__ = 'ramon'

comparison = 0


def choose_pivot_last(A, l, r):
    pivotIndex = r-1
    A[l], A[pivotIndex] = A[pivotIndex], A[l]
    return partition_last_element(A, l, r)


def partition_last_element(A, l, r):
    #input = A[l ... r]
    p = A[l]
    i = l+1

    for j in range(l+1, r):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[l], A[i-1] = A[i-1], A[l]
    return i


def quicksort_last_element(A, l, r):
    global comparison

    if l < r:
        comparison += r-l-1
        q = choose_pivot_last(A, l, r)
        quicksort_last_element(A, l, q-1)
        quicksort_last_element(A, q, r)
        return A, comparison

'''
def partition_last_element(A, l, r):
    #input = A[l ... r]
    p = A[r]
    i = l-1

    for j in range(l, r):
        if A[j] <= p:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort_last_element(A, l, r):
    global comparison

    if l < r:
        comparison += r-l-1
        q = partition_last_element(A, l, r)
        quicksort_last_element(A, l, q-1)
        quicksort_last_element(A, q+1, r)
        return A, comparison
'''

#array = [2, 3, 8, 1, 7, 4, 6, 5]
#A, c = quicksort_last_element(array, 0, len(array)-1)
#print(A)
#print(c)


'''
Copiando el fichero quicksort en el array A
'''

A = []

with open("QuickSort.txt", "r") as my_file:
    for line in my_file:
        A.append(int(line.strip()))

sorted_array, comparisons = quicksort_last_element(A, 0, len(A))
print("Sorted Array:" + str(sorted_array) + "\nwith " + str(comparisons) + " comparisons")