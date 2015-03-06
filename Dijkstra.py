__author__ = 'ramon'


class Node(object):
    def __init__(self, u=0, v=None, w=None):    # u=key_node, v=pointed_node, w=weight(u,v)
        self.u = u
        if v is None:
            self.v = []
        else:
            self.v = v
        if w is None:
            self.w = []
        else:
            self.w = w

    def __str__(self):
        return "({0}->{1},{2})".format(self.u, self.v, self.w)


def get_input(filename):
    graph_map = []

    for line in open(filename, 'r').readlines():
        values = line.split()
        key1 = values.pop(0)
        g = Node()
        g.u = int(key1)
        for set in values:
            vals = set.split(',')
            g.v.append(int(vals[0]))
            g.w.append(int(vals[1]))

        graph_map.append(g)
        #print(g)

    return graph_map


def dijkstra(graph_map):
    S = list()     # vertices processed so far  [Node()]*len(graph_map)
    S.append(graph_map[0].u)
    print(S)
    D = [float("inf")]*len(graph_map)   # vector de distancias
    print(D)
    P = dict()  # P[v] contiene el vértice inmediato anterior a v en el camino más corto

    for i in range(0, len(graph_map[0].w)):
        if graph_map[0].w[i] is not None:
            D[i] = graph_map[0].w[i]

    for i in range(0, len(graph_map)-1):
        w = D.index(min(D))
        new_node_position = graph_map[i].v[w] - 1
        S.append(graph_map[i].v[w])
        print('S=', S)
        for j in range(0, len(graph_map[new_node_position].w)):
            v = graph_map[new_node_position].v[j]
            if D[w] + graph_map[new_node_position].w[j] < D[v]:
                D[v] = D[w] + graph_map[new_node_position].w[j]
                P[v] = w
                print('D=', D, 'P=', P)



graph_map = get_input("disktra_test1.txt")
for i in graph_map:
    print(i)

dijkstra(graph_map)