__author__ = 'Ramon'

import sys


def get_input(filename):
    array = list()

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]

        if len(values) == 2:
            print("# of nodes:", values.pop(0), "# of edges:", values.pop(0))
        else:
            key1 = values.pop(0)
            key2 = values.pop(0)
            key3 = values.pop(0)

            vev = VeV(key1, key2, key3)
            array.append(vev)

    return array


def find_min(G, vertex):
    e_array = list()
    bib = {}

    print("vertex = ", vertex)

    for i in G:
        if i.vertex1 == vertex or i.vertex2 == vertex:
            e_array.append(i.edge)

            if not i.edge in bib:
                bib[i.edge] = []

            if i.vertex1 == vertex:
                bib[i.edge].extend([i.vertex2])
            else:
                bib[i.edge].extend([i.vertex1])

            G.remove(i)

    cheapest_edge = min(e_array)
    return cheapest_edge, bib[cheapest_edge][0]


def Prim(G):
    X = [G[0].vertex1]
    T = list()

    while G is not None:
        minimum, v2 = find_min(G, X[len(X)-1])
        T.append(minimum)
        X.append(v2)

    return X


class VeV():    # Vertex_edge_Vertex
    def __init__(self, vertex1, vertex2, edge):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.edge = edge

    def __str__(self):
        return str(self.vertex1) + "---" + str(self.edge) + "---" + str(self.vertex2)


if __name__ == '__main__':
    #a = get_input("edges.txt")
    a = list()
    a.append(VeV(1, 2, 1))
    a.append(VeV(2, 4, 2))
    a.append(VeV(4, 1, 3))
    a.append(VeV(4, 3, 5))
    a.append(VeV(3, 1, 4))
    #for i in a:
    #    print(i)
    print(Prim(a))
