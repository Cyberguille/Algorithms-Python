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
    stack = [iter(range(len(graph_map), 0, -1))]

    while stack:
        try:
            child = next(stack[0])
            print(child)
            if visited[child-1] is False:
                stack.append(iter(graph_map[child]))
                counter += 1
                visited[child-1] = True
        except StopIteration:
            stack.pop()
        t += 1
        finished_time[start-1] = t

    return finished_time


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
    global t, s, counter, visited, finished_time
    t = 0   # for finishing times in 1st pass. It stands for the # of nodes processed so far.
    counter = 0
    length = len(graph_map)
    #length = max(graph_map.keys())
    visited = [False]*length  # size of the graph
    finished_time = [0]*length


def kosaraju(graph_map):
    graph_map_rev = transpose_graph(graph_map)
    DFS(graph_map_rev, len(graph_map))
    graph_finish = get_graph_finish(graph_map_rev)
    restart_global_variables()
    return DFS(graph_finish, len(graph_finish))


graph_map = get_input("test3.txt")
#print(graph_map)

#Global variables
t = 0   # for finishing times in 1st pass. It stands for the # of nodes processed so far.
counter = 0
length = len(graph_map)
#length = max(graph_map.keys())
#print(length)
#print(max(graph_map.keys()))
visited = [False]*length  # size of the graph
finished_time = [0]*length
#DFS_Loop(graph_map)
#for i in range(0, len(graph_map)):
#    print(finished_time[i])

gm = kosaraju(graph_map)
gm.reverse()
print(gm)


