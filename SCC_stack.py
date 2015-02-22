__author__ = 'ramon'


def get_input(filename):
    graph_map = {}

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        key1 = values.pop(0)
        key2 = values.pop(0)

        if not key1 in graph_map:
            graph_map[key1] = []

        if not key2 in graph_map:
            graph_map[key2] = []

        graph_map[key1].extend([key2])

    return graph_map


def DFS(graph_map, start):
    global t, finished_time, visited, counter

    visited[start-1] = True

    for child in graph_map[start]:
        if visited[child-1] is False:
            DFS(graph_map, child)
            counter += 1
    t += 1
    finished_time[start-1] = t


def DFS_Loop(graph_map):
    global visited, counter
    count_list = []

    i = len(graph_map)  # max(graph_map.keys())
    for i in reversed(range(1, i+1)):
        if visited[i-1] is False:
            counter = 1
            DFS(graph_map, i)
            count_list.append(counter)

    return count_list


def transpose_graph(graph_map):
    # graph_map_rev = {v: k for k, v in graph_map.items()}
    graph_map_rev = {}
    for k in graph_map:
        if not k in graph_map_rev:
            graph_map_rev[k] = []
        for kk in graph_map[k]:
            if not kk in graph_map_rev:
                graph_map_rev[kk] = []
            graph_map_rev[kk].extend([k])

    #print(graph_map_rev)
    return graph_map_rev


def get_graph_finish(graph_map_rev):
    graph_finish = {}
    for k in graph_map_rev:
        if not finished_time[k-1] in graph_finish:
            graph_finish[finished_time[k-1]] = []
        for kk in graph_map_rev[k]:
            if not finished_time[kk-1] in graph_finish:
                graph_finish[finished_time[kk-1]] = []
            #print(k, kk, finished_time[k-1], finished_time[kk-1])
            graph_finish[finished_time[kk-1]].extend([finished_time[k-1]])

    #print(graph_finish)
    return graph_finish


def restart_global_variables():
    global t, counter, visited, finished_time
    t = 0   # for finishing times in 1st pass. It stands for the # of nodes processed so far.
    counter = 0
    lenght = len(graph_map)
    #lenght = max(graph_map.keys())
    visited = [False]*lenght  # size of the graph
    finished_time = [0]*lenght


def kosaraju(graph_map):
    graph_map_rev = transpose_graph(graph_map)
    DFS_Loop(graph_map_rev)
    graph_finish = get_graph_finish(graph_map_rev)
    restart_global_variables()
    return DFS_Loop(graph_finish)


graph_map = get_input("test1.txt")
#print(graph_map)

#Global variables
t = 0   # for finishing times in 1st pass. It stands for the # of nodes processed so far.
counter = 0
lenght = len(graph_map)
#lenght = max(graph_map.keys())
#print(lenght)
#print(max(graph_map.keys()))
visited = [False]*lenght  # size of the graph
state = []*lenght
finished_time = [0]*lenght
#DFS_Loop(graph_map)
#for i in range(0, len(graph_map)):
#    print(finished_time[i])

gm = kosaraju(graph_map)
#print(gm)


def partition(A, l, r):
    #input = A[l ... r]
    p = A[l]
    i = l+1

    for j in range(l+1, r):
        if A[j] > p:    # changing (A[j] < p) with (A[j] > p) to sort in reverse
            A[i], A[j] = A[j], A[i]
            i += 1

    A[l], A[i-1] = A[i-1], A[l]
    return i


def choose_pivot_middle(A, l, r):
    first = l

    if (r-l) % 2 is 0:
        mid = ((r-l)//2 - 1) + l
    else:
        mid = ((r-l)//2) + l

    last = r-1

    B = []
    B.append(A[first])
    B.append(A[mid])
    B.append(A[last])

    if B[2] < B[0]:
        B[0], B[2] = B[2], B[0]
    if B[1] < B[0]:
        B[1], B[0] = B[0], B[1]
    if B[2] < B[1]:
        B[2], B[1] = B[1], B[2]

    if A[first] == B[1]:
        pivotIndex = first
    elif A[mid] == B[1]:
        pivotIndex = mid
    else:
        pivotIndex = last

    A[l], A[pivotIndex] = A[pivotIndex], A[l]
    return partition(A, l, r)


def quicksort_middle_element(A, l, r):
    if l < r:
        q = choose_pivot_middle(A, l, r)
        quicksort_middle_element(A, l, q-1)
        quicksort_middle_element(A, q, r)
        return A

sorted_array = quicksort_middle_element(gm, 0, len(gm))
print(sorted_array)