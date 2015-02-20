__author__ = 'ramon'


class Node:
    def __init__(self):
        self.key = 0
        self.value = []
        self.visited = False
        self.leader = 0
        self.finishing_time = 0


#Global variables
t = 0   # for finishing times in 1st pass. It stands for the # of nodes processed so far.
s = Node()    # for leaders in 2nd pass. It stands for the current source vertex.


def get_input(filename):
    graph_map = {}

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        key = values.pop(0)
        if key in graph_map and node is not None:
            node.value.extend(values)
        else:
            node = Node()
            node.key = key
            node.value = values
            graph_map[key] = node
        #print(key, node.value)
    return graph_map


def DFS(graph_map, node):
    global t
    global s

    node.visited = True
    node.leader = s.key
    while node in graph_map:
        if node.visited is False:
            DFS(graph_map, node)
    t += 1
    node.finishing_time = t


def DFS_Loop(graph_map):
    global s

    i = max(graph_map.keys())
    while i >= 1:
        if graph_map[i].visited is False:
            s = graph_map[i]
            DFS(graph_map, s)
        i -= 1


def kosaraju(graph_map):
    graph_map_rev = {v: k for k, v in graph_map.items()}
    print(graph_map_rev)

graph_map = get_input("test1.txt")
DFS_Loop(graph_map)
print(t)
print(kosaraju(graph_map))
