__author__ = 'ramon'


def DFSvisit(G, v, visited, order, component):
    visited[v] = component
    for w in G[v]:
        if not visited[w]:
            DFSvisit(G, w, visited, order, component)
    order.append(v)


def DFS(G, sequence, visited, order):
    components = 0
    for v in sequence:
        if not visited[v]:
            components += 1
            DFSvisit(G, v, visited, order, components)

n, m =(int(i) for i in input().strip().split())

G = [[] for i in range(n)]
Gt = [[] for i in range(n)]
for i in range(m):
    a, b = (int(i) for i in input().strip().split())
    G[a-1].append(b-1)
    Gt[b-1].append(a-1)

order = []
components = [0]*n

DFS(G, range(n), [0]*n, order)
DFS(Gt, reversed(order), components, [])

print(max(components))
print(components)