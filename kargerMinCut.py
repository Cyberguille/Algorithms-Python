__author__ = 'Ramon'

import random
import copy


def get_input(filename):
    graph_map = {}

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        key = values.pop(0)
        graph_map[key] = values

    return graph_map


def karger_v1(A):
    # pick a remaining edge (u,v) uniformly at random
    u = random.randint(0, len(A)-1)
    v = random.randint(0, len(A[u])-1)
    #u, v = 4, 2
    print('A[', u, '][', v, '] =', A[u][v])

    # merge (or contract) u and v into a single vertex
    temp = A[u][v]

    #for k in range(0, len(A[temp-1])):
    #    if A[temp-1][k] == (u+1):
    #        A[temp-1].remove(A[temp-1][k])
    #        break

    A[u] += A[temp-1]
    A[u].remove(A[u][v])    # edge between node 5 and 2
    A[u].remove(u+1)    # edge between node 2 and 5

    # remove self loops
    #for k in range(0, len(A[u])):
    #    if A[u][k] == u:
    #        A[u].remove(A[u][k])
    #        break

    # duplicate sub-array (node) to complete merge and not loosing the order of the elements in array
    # (so I don't have to use keys)
    #A.remove(A[temp-1])    #instead of deleting it, I'm making a duplicate
    # the problem with this method is that the total size will increase every-time a merge occurs
    A[temp-1] = A[u]

    print(A)


def karger_v2(graph_map):

    while len(graph_map) > 2:

        u = list(graph_map.keys())[random.randint(0, len(graph_map)-1)]
        v = list(graph_map[u])[random.randint(0, len(graph_map[u])-1)]
        #u, v = 1, 2
        #print('u =', u, 'v =', v)
        #print(list(graph_map.keys()))

        # merge (or contract) u and v into a single vertex
        graph_map[u].extend(graph_map[v])
        #print('graph_map[u] =', graph_map[u])
        #print('graph_map[v] =', graph_map[v])

        for i in graph_map[v]:
            # searching in each of the arrays that the node "v" was pointing to
            temp = graph_map[i]

            # redirecting pointers (from the node that's going to be deleted to the merged one)
            for j in range(0, len(temp)):
                if temp[j] == v:
                    temp[j] = u

        # delete entry for second vertex	from hash map
        del graph_map[v]

        # remove self loops
        while u in graph_map[u]:
            graph_map[u].remove(u)

    #print(graph_map)

    return len(graph_map[list(graph_map.keys())[0]])


def run_min_cut(graph_map, n):
    minimum_cut_value = karger_v2(copy.deepcopy(graph_map))
    #looping for sample
    for i in range(1, n):
        x = karger_v2(copy.deepcopy(graph_map))
        if x < minimum_cut_value:
            minimum_cut_value = x

    return minimum_cut_value


A = get_input("kargertest1.txt")
#print(A)
#karger_v1(A)
print(run_min_cut(A, 100))