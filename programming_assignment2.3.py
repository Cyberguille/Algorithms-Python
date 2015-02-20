__author__ = 'ramon'

comparison = 0


def choose_pivot_middle(A, l, r):
    #print(A)
    '''
    first = A[l]

    if (r-l) % 2 is 0:
        mid = A[((r-l)//2 - 1) + l]
    else:
        mid = A[((r-l)//2) + l]

    last = A[r-1]
    '''

    first = l

    if (r-l) % 2 is 0:
        mid = ((r-l)//2 - 1) + l
    else:
        mid = ((r-l)//2) + l

    last = r-1
    #print('first=', str(A[first]), 'mid=', str(A[mid]), 'last=', str(A[last]))
    #print(A)

    B = []
    B.append(A[first])
    B.append(A[mid])
    B.append(A[last])

    #print(B)
    if B[2] < B[0]:
        B[0], B[2] = B[2], B[0]
    if B[1] < B[0]:
        B[1], B[0] = B[0], B[1]
    if B[2] < B[1]:
        B[2], B[1] = B[1], B[2]

    #print(B)

    if A[first] == B[1]:
        pivotIndex = first
    elif A[mid] == B[1]:
        pivotIndex = mid
    else:
        pivotIndex = last

    #print('first=', str(A[first]), 'mid=', str(A[mid]), 'last=', str(A[last]))
    #print(A)
    #print(pivotIndex)
    #print('*************************************************')
    '''
    if (first > mid and first < last)or(first > last and first < mid):
        pivotIndex = l
        print(pivotIndex)
    elif (mid > first and mid < last)or(mid > last and mid < first):
        if len(A) % 2 is 0:
            pivotIndex = ((r-l)//2 - 1) + l
            print(pivotIndex)
        else:
            pivotIndex = ((r-l)//2) + l
            print(pivotIndex)
    else:
        pivotIndex = r-1
        print(pivotIndex)

    print('l=', l, 'A[l]=', first, 'm=', ((r-l)//2 - 1) + l, 'A[m]=', mid, 'r=', r, 'A[r]=', last, 'A[p]=', A[pivotIndex], 'p=', pivotIndex)
    '''

    A[l], A[pivotIndex] = A[pivotIndex], A[l]
    return partition_middle_element(A, l, r)


def partition_middle_element(A, l, r):
    #input = A[l ... r]
    p = A[l]
    i = l+1

    for j in range(l+1, r):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[l], A[i-1] = A[i-1], A[l]
    return i


def quicksort_middle_element(A, l, r):
    global comparison

    if l < r:
        comparison += r-l-1
        q = choose_pivot_middle(A, l, r)
        quicksort_middle_element(A, l, q-1)
        quicksort_middle_element(A, q, r)
        return A, comparison


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

sorted_array, comparisons = quicksort_middle_element(A, 0, len(A))
print("Sorted Array:" + str(sorted_array) + "\nwith " + str(comparisons) + " comparisons")