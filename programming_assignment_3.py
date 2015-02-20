__author__ = 'Ramon'

'''
Download the text file here. (Right click and save link as)
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1
to 200. The first column in the file represents the vertex label, and the particular row (other entries except the
first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like :
"6 155 56 52 120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with)
the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above
graph to compute the min cut (i.e., the minimum-possible number of crossing edges). (HINT: Note that you'll have to
figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph
from the old every time there's an edge contraction. But you should also think about more efficient implementations.)
(WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and
remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer
is 5, just type 5 in the space provided.

SCORE: 5!
'''

import random
import copy


def get_input(filename):
    graph_map = {}

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        key = values.pop(0)
        graph_map[key] = values

    return graph_map


def karger(graph_map):

    while len(graph_map) > 2:

        u = list(graph_map.keys())[random.randint(0, len(graph_map)-1)]
        v = list(graph_map[u])[random.randint(0, len(graph_map[u])-1)]

        # merge (or contract) u and v into a single vertex
        graph_map[u].extend(graph_map[v])

        for i in graph_map[v]:
            # searching in each of the arrays that the node "v" was pointing to
            temp = graph_map[i]

            # redirecting pointers (from the node that's going to be deleted to the merged one)
            for j in range(0, len(temp)):
                if temp[j] == v:
                    temp[j] = u

        # delete entry for second vertex from hash map
        del graph_map[v]

        # remove self loops
        while u in graph_map[u]:
            graph_map[u].remove(u)

    return len(graph_map[list(graph_map.keys())[0]])


def run_min_cut(graph_map, n):
    minimum_cut_value = karger(copy.deepcopy(graph_map))
    #looping for sample
    for i in range(1, n):
        x = karger(copy.deepcopy(graph_map))
        if x < minimum_cut_value:
            minimum_cut_value = x

    return minimum_cut_value


A = get_input("kargerMinCut.txt")
print(run_min_cut(A, 100))