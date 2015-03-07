__author__ = 'Ramon'

'''
Heap minimum property: at every node X, key[X] <= all keys of X's children.
'''


class heap_min():
    def __init__(self, array):
        self.tree = list()
        for i in array:
            self.insert(i)

    def __str__(self):
        return str(self.tree)

    def insert(self, value):
        self.tree.append(value)
        value_index = len(self.tree)-1
        self.bubble_up(value_index)

    def bubble_up(self, value_index):
        parent_index = (value_index-1)//2
        if self.tree[value_index] < self.tree[parent_index]:
            self.tree[value_index], self.tree[parent_index] = self.tree[parent_index], self.tree[value_index]
            self.bubble_up(parent_index)

    def bubble_down(self, value_index):
        child_index1 = (value_index+1)*2 - 1
        child_index2 = (value_index+1)*2
        if child_index2 < len(self.tree):
            if self.tree[child_index1] < self.tree[child_index2]:
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


'''
Heap maximum property: at every node X, key[X] >= all keys of X's children.
'''


class heap_max():
    def __init__(self, array):
        self.tree = list()
        for i in array:
            self.insert(i)

    def __str__(self):
        return str(self.tree)

    def insert(self, value):
        self.tree.append(value)
        value_index = len(self.tree)-1
        self.bubble_up(value_index)

    def bubble_up(self, value_index):
        parent_index = (value_index-1)//2
        if self.tree[value_index] > self.tree[parent_index]:
            self.tree[value_index], self.tree[parent_index] = self.tree[parent_index], self.tree[value_index]
            self.bubble_up(parent_index)

    def bubble_down(self, value_index):
        child_index1 = (value_index+1)*2 - 1
        child_index2 = (value_index+1)*2
        if child_index2 < len(self.tree):
            if self.tree[child_index1] > self.tree[child_index2]:
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

'''
a = [4, 4, 8, 9, 4, 12, 9, 11, 13]
hmin = heap_min(a)
print(hmin)
hmin.insert(7)
print(hmin)
hmin.insert(10)
print(hmin)
hmin.insert(5)
print(hmin)
print(hmin.extract())
print(hmin)
'''
b = [4, 4, 8, 9, 4, 12, 9, 11, 13]
hmax = heap_max(b)
print(hmax)
hmax.insert(7)
print(hmax)
hmax.insert(10)
print(hmax)
hmax.insert(5)
print(hmax)
print(hmax.extract())
print(hmax)
