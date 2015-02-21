__author__ = 'ramon'


def get_input(filename):
    graph_map = {}

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        key = values.pop(0)
        if key in graph_map:
            graph_map[key].extend(values)
        else:
            graph_map[key] = values

    return graph_map


def DFS(graph_map, start):
    global t, s, finished_time, visited, counter

    visited[start-1] = True

    for child in graph_map[start]:
        if visited[child-1] is False:
            DFS(graph_map, child)
            counter += 1
    t += 1
    finished_time[start-1] = t


def DFS_Loop(graph_map):
    global s, visited, counter
    count_list = []

    i = len(graph_map)  # max(graph_map.keys())
    for i in reversed(range(1, i+1)):
        if visited[i-1] is False:
            s = i
            counter = 1
            DFS(graph_map, s)
            count_list.append(counter)

    return count_list


def transpose_graph(graph_map):
    # graph_map_rev = {v: k for k, v in graph_map.items()}
    graph_map_rev = {}
    for k in graph_map:
        for kk in graph_map[k]:
            if not kk in graph_map_rev:
                graph_map_rev[kk] = []
            graph_map_rev[kk].extend([k])

    #print(graph_map_rev)
    return graph_map_rev


def get_graph_finish(graph_map_rev):
    graph_finish = {}
    for k in graph_map_rev:
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
    s = 0    # for leaders in 2nd pass. It stands for the current source vertex.
    counter = 0
    #lenght = int(input("Enter the lenght of the array: "))
    visited = [False]*len(graph_map)  # size of the graph
    finished_time = [0]*len(graph_map)


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
s = 0    # for leaders in 2nd pass. It stands for the current source vertex.
counter = 0
#lenght = int(input("Enter the lenght of the array: "))
visited = [False]*len(graph_map)  # size of the graph
finished_time = [0]*len(graph_map)

#DFS_Loop(graph_map)
#for i in range(0, len(graph_map)):
#    print(finished_time[i])

gm = kosaraju(graph_map)
print(gm)