__author__ = 'Ramon'

import timeit

#name = 'file.txt'  # Name of text file coerced with +.txt
#file = open(name, 'w')   # Trying to create a new file or open one


def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    #print('n1 = q - p + 1 =', n1, 'n2 = r - q = ', n2)
    #file.write('n1 = q - p + 1 ='+str(n1)+' n2 = r - q = '+str(n2)+'\n')
    L = []
    R = []

    for i in range(0, n1):
        L.append(A[p+i-1])
    for j in range(0, n2):
        R.append(A[q+j])

    #print('L=', L, 'R=', R)
    #file.write('L='+str(L)+' R='+str(R)+'\n')
    # placing sentinels
    # the sentinel should be infinite: a number so big that any other number in the array is bigger than it
    L.append(9999999)  # L[n1+1] = 9999999
    R.append(9999999)  # R[n2+1] = 9999999
    i = j = 0

    for k in range(p-1, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A


def merge_sort(A, p, r):
    sorted_A = 0
    if p < r:
        q = int((p+r-1)/2)
        #print('q = (', p, '+', r, '- 1)/2 =', q)
        #file.write('q = ('+str(p)+'+'+str(r)+'- 1)/2 ='+str(q)+'\n')
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        #print('A=', A, 'p=', p, 'q=', q, 'r=', r)
        #file.write('A='+str(A)+' p='+str(p)+' q='+str(q)+' r='+str(r)+'\n')
        sorted_A = merge(A, p, q, r)
        #print(sorted_A)
        #file.write('\nSorted A = '+str(sorted_A)+'\n\n')
    return sorted_A


def main1():
    #A = [8, 7, 6, 5, 4, 3, 2, 1]
    A = list(range(0, 10001, 1))
    A.reverse()
    sorted_A = merge_sort(A, 1, len(A))
    #print(sorted_A)

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main1()', setup='from __main__ import main1', number=1)
print('total time 1=', result*1000, 'ms')
#file.write('Total Running Time = '+str(result*1000)+' ms')
#file.close()


def main2():
    #A = [8, 7, 6, 5, 4, 3, 2, 1]
    A = list(range(0, 1001, 1))
    A.reverse()
    sorted_A = merge_sort(A, 1, len(A))
    #print(sorted_A)

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main2()', setup='from __main__ import main2', number=1)
print('total time 2=', result*1000, 'ms')


def main3():
    A = [8, 7, 6, 5, 4, 3, 2, 1]
    sorted_A = merge_sort(A, 1, len(A))
    #print(sorted_A)

# result is the time (in seconds) to run the whole loop
result = timeit.timeit('main3()', setup='from __main__ import main3', number=1)
print('total time 3=', result*1000, 'ms')