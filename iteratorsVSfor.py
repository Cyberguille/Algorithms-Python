__author__ = 'ramon'

'''
One of the cool things about Python is that iterators are just a normal datatype. Although one usually uses for loops
and comprehensions to iterate, there is nothing to stop you from doing the iteration manually if that is convenient.
One reason it might be convenient is to avoid deep recursion, by replacing it with an explicit stack.

While this does "take away the recursion", it does not significantly complicate the program, and the recursive
structure is still evident. Python simply does not recurse gracefully, so this sort of transformation is often useful.
'''


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

graph_map = get_input("test3.txt")
print(graph_map)

length = len(graph_map)

print('FOR LOOP')
# with for loop
for i in range(1, length+1):
    for child in graph_map[i]:
        print('key=', i, 'child', child)

print('ITERATORS')
# with iterators
for i in range(1, length+1):
    it = iter(graph_map[i])
    try:
        while it:
            child = next(it)
            print('key=', i, 'child', child)
    except StopIteration:
        pass

# traversing list from end to start
A = [1, 2, 3]
for i in range(len(A), 0, -1):
    print(i)

# stacked iterators (back to front)
print('stacked iterators')
stack = [iter(range(length, 0, -1))]
while stack:
    try:
        child = next(stack[0])
        print('key=', child, 'child', graph_map[child])
        stack.append(iter(graph_map[child]))

    except StopIteration:
        stack.pop()


# stacked iterators (front to back)
print('stacked iterators')
stack = [iter(range(1, length+1))]
while stack:
    try:
        child = next(stack[0])
        print('key=', child, 'child', graph_map[child])
        stack.append(iter(graph_map[child]))

    except StopIteration:
        stack.pop()