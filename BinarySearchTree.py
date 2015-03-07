__author__ = 'Ramon'

'''
Search trees are data structures that support many dynamic-set operations, including SEARCH,MINIMUM,MAXIMUM,PREDECESSOR,
SUCCESSOR,INSERT,and DELETE. Thus, a search tree can be used both as a dictionary and as a priority queue.

Basic operations on a binary search tree take time proportional to the height of the tree.
For a complete binary tree with n nodes, such operations run inO(lgn) worst-case time. If the tree is a linear chain
of n nodes, however, the same operations takeO(n) worst-case time.
The expected height of a randomly built binary search tree is O(lgn), so that basic dynamic-set
operations on such a tree takeO(lgn)time on average.

The keys in a binary search tree are always stored in such a way as to satisfy the binary-search-tree property:

Let x be a node in a binary search tree. If y is a node in the left subtree of x,then key[y] ≤ key[x].
If y is a node in the right subtree of x,then key[x] ≤ key[y].
'''


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        lk, rk, pk = None, None, None
        if self.left is not None:
            lk = self.left.key
        if self.right is not None:
            rk = self.right.key
        if self.parent is not None:
            pk = self.parent.key
        return str(self.key)+':('+str(lk)+','+str(rk)+','+str(pk)+')'


class BinarySearchTree:
    def __init__(self, array=list()):
        self.tree = list()
        self.root = Node(array.pop(0))
        self.tree.append(self.root)
        for i in array:
            self.insert(i)

    def __str__(self):
        print_array = list()
        for i in self.tree:
            print_array.append(str(i))
        return str(print_array)

    def insert(self, key):
        node = Node(key)
        parent = self.search(node.key)
        if node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.parent = parent
        self.tree.append(node)

    def search(self, key):
        seeker = self.root    # start at the root node
        parent = None   # since we are on root
        return self.traverse(seeker, key, parent)

    def traverse(self, seeker, key, parent):
        if seeker is None:
            return parent   # in order to insert a new node
        if seeker.key == key:
            return seeker
        if key < seeker.key:
            return self.traverse(seeker.left, key, seeker)
        else:
            return self.traverse(seeker.right, key, seeker)


def test():
    array = [3,1,5,2,4,6]
    bst = BinarySearchTree(array)
    print(bst)
    bst.insert(7)
    print(bst)
    print(bst.search(5))


if __name__ == '__main__':
    test()