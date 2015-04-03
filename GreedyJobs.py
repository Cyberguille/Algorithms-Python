__author__ = 'Ramon'

import random


# insertion sort no se usa pero funciona OK
def insertion_sort(jobs):
    for j in range(1, len(jobs)):
        key = jobs[j]
        i = j-1
        while i >= 0 and (jobs[i].difference < key.difference or (jobs[i].difference == key.difference and
                                                                          jobs[i].weight < key.weight)):
            jobs[i+1] = jobs[i]
            i -= 1
        jobs[i+1] = key
    return jobs
#-----------------------------------------------------------------------------------------------------------------------


# QUICK_SORT
def partition(A, l, r, ratio):
    #input = A[l ... r]
    p = A[l]
    i = l+1

    for j in range(l+1, r):
        if ratio:
            x = A[j].ratio >= p.ratio
        else:
            x = (A[j].difference > p.difference or (A[j].difference == p.difference and A[j].weight > p.weight))
        if x:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[l], A[i-1] = A[i-1], A[l]
    return i


def choose_pivot_random(A, l, r, ratio):
    pivotIndex = random.randint(l, r-1)
    A[l], A[pivotIndex] = A[pivotIndex], A[l]
    return partition(A, l, r, ratio)


def quicksort(A, l, r, ratio):
    if l < r:
        q = choose_pivot_random(A, l, r, ratio)
        quicksort(A, l, q-1, ratio)
        quicksort(A, q, r, ratio)
        return A
#-----------------------------------------------------------------------------------------------------------------------


def get_input(filename):
    array = list()

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]

        if len(values) == 1:
            print("# of jobs:", values.pop(0))
        else:
            key1 = values.pop(0)
            key2 = values.pop(0)

            job = Job(key1, key2)
            array.append(job)

    return array


class Job():
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.difference = weight - length
        self.ratio = weight/length

    def __str__(self):
        return str(self.weight) + ", " + str(self.length) + ", " + str(self.difference) + ", " + str(self.ratio)


if __name__ == '__main__':
    a = get_input("jobs.txt")
    # Orber by ratio: True, Order by difference: False
    b = quicksort(a, 0, len(a), False)
    #b = insertion_sort(a)

    completion_times = 0
    weighted_completion_times = 0

    for i in b:
        completion_times += i.length
        weighted_completion_times += i.weight * completion_times
        #print(i)
    print("weighted_completion_times = " + str(weighted_completion_times))

# Answers:
#   Ordered by difference: 69119377652
#   Ordered by ratio: 67311454237