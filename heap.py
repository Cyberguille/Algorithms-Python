__author__ = 'Ramon'

'''
Heap property: at every node X, key[X] <= (if min) or >= (if max) all keys of X's children.
'''


class heap():
    def __init__(self, array, hmax=False):
        self.tree = list()
        self.max = hmax
        for i in array:
            self.insert(i)

    def __str__(self):
        return str(self.tree)

    def insert(self, value):
        self.tree.append(value)
        value_index = len(self.tree)-1
        self.bubble_up(value_index)

    def bubble_up(self, value_index):
        if value_index > 0:
            parent_index = (value_index-1)//2
            if self.max is True:
                flag = self.tree[value_index] > self.tree[parent_index]
            else:
                flag = self.tree[value_index] < self.tree[parent_index]
            if flag:
                self.tree[value_index], self.tree[parent_index] = self.tree[parent_index], self.tree[value_index]
                self.bubble_up(parent_index)

    def bubble_down(self, value_index):
        child_index1 = (value_index+1)*2 - 1
        child_index2 = (value_index+1)*2
        if child_index2 < len(self.tree):
            if self.max is True:
                flag = self.tree[child_index1] > self.tree[child_index2]
            else:
                flag = self.tree[child_index1] < self.tree[child_index2]
            if flag:
                self.tree[value_index], self.tree[child_index1] = self.tree[child_index1], self.tree[value_index]
                self.bubble_down(child_index1)
            else:
                self.tree[value_index], self.tree[child_index2] = self.tree[child_index2], self.tree[value_index]
                self.bubble_down(child_index2)
        elif child_index1 < len(self.tree):
            self.tree[value_index], self.tree[child_index1] = self.tree[child_index1], self.tree[value_index]
            self.bubble_down(child_index1)

    def extract(self):
        self.tree[0], self.tree[-1] = self.tree[-1], self.tree[0]
        root = self.tree.pop()
        self.bubble_down(0)
        return root


def test():
    c = [4, 4, 8, 9, 4, 12, 9, 11, 13]
    h = heap(c, True)
    print(h)
    h.insert(7)
    print(h)
    h.insert(10)
    print(h)
    h.insert(5)
    print(h)
    print(h.extract())
    print(h)

if __name__ == '__main__':
    test()