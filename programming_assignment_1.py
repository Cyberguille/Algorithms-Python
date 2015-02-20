__author__ = 'ramon'
'''
The file IntegerArray.txt contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order,
with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith
entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the
video lectures. The numeric answer for the given input file should be typed in the space below.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas /
any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.
(We do not require you to submit your code, so feel free to use any programming language you want --- just type
the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising.
Then post your best test cases to the discussion forums to help your fellow students!]

SCORE: 5!
'''


def merge_countSplitInv(B, C):
    i, j, count = 0, 0, 0
    D = []
    #print(B, C)
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
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


#A = [1, 3, 5, 2, 4, 6, 1]  # repeated numbers ANS = 8

#A = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]  # 15 numbers ANS = 56

#A = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21,
#     29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]    # 50 numbers ANS = 590

#A = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6,
#     79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72,
#     91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30,
#     22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]    # 100 numbers ANS = 2372

A = []

with open("IntegerArray.txt", "r") as my_file:
    for line in my_file:
        A.append(int(line.strip()))

sorted_array, inversions = merge_count(A)
print("Sorted Array:" + str(sorted_array) + "\nwith " + str(inversions) + " inversions")