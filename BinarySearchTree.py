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

    # worst case running time = O(height)
    def insert(self, key):
        node = Node(key)
        seeker = self.root    # start at the root node
        parent = None
        while (seeker is not None) and (seeker.key != key):
            parent = seeker
            if key < seeker.key:
                seeker = seeker.left
            else:
                seeker = seeker.right
        if seeker is None:
            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node
            node.parent = parent
            self.tree.append(node)

    def delete(self, key):
        seeker = self.search(key)
        parent = seeker.parent
        # if the node exists
        if seeker is not None:
            # difficult case (seeker has 2 children)
            if seeker.left is not None and seeker.right is not None:
                pred = self.predecessor(seeker)
                print(seeker, pred)
                self.xchange(seeker, pred)
                print(seeker, pred)
            # medium case (seeker has 1 child)
            if seeker.left is not None or seeker.right is not None:
                if seeker.left is not None:
                    seeker, seeker.left = seeker.left, seeker
                else:
                    seeker, seeker.right = seeker.right, seeker
            # at this point it all arrives to the easy case (seeker has no children)
            if seeker == parent.right:
                parent.right = None
            else:
                parent.left = None
            self.tree.remove(seeker)

    def xchange(self, node1, node2):
        node1, node2 = node2, node1
        node1.key, node2.key = node2.key, node1.key
        node1.parent, node2.parent = node2.parent, node1.parent
        node1.left, node2.left = node2.left, node1.left
        node1.right, node2.right = node2.right, node1.right

    # worst case running time = O(height)
    def search(self, key):
        seeker = self.root    # start at the root node
        while (seeker is not None) and (seeker.key != key):
            if key < seeker.key:
                seeker = seeker.left
            else:
                seeker = seeker.right
        return seeker

    def min(self):
        return self.min_subtree(self.root)

    def max(self):
        return self.max_subtree(self.root)

    # worst case running time = O(height)
    def min_subtree(self, subtree_root):
        seeker = subtree_root    # start at the root node of the subtree
        while seeker.left is not None:
            seeker = seeker.left
        return seeker

    # worst case running time = O(height)
    def max_subtree(self, subtree_root):
        seeker = subtree_root    # start at the root node of the subtree
        while seeker.right is not None:
            seeker = seeker.right
        return seeker

    # running time = O(n)
    def in_order_traversal(self, start_node):
        if start_node is not None:
            self.in_order_traversal(start_node.left)
            print(start_node.key)
            self.in_order_traversal(start_node.right)

    # worst case running time = O(height)
    def successor(self, node):
        if node.right is not None:
            return self.min_subtree(node.right)
        seeker = node.parent
        # while it hasn't arrived to the root and it hasn't turned right
        # (if it's the right child of parent then it's key is bigger than parent's)
        while seeker is not None and node == seeker.right:
            node = seeker
            seeker = seeker.parent
        return seeker

    # worst case running time = O(height)
    def predecessor(self, node):
        if node.left is not None:
            return self.max_subtree(node.left)
        seeker = node.parent
        # while it hasn't arrived to the root and it hasn't turned left
        # (if it's the left child of parent then it's key is lower than parent's)
        while seeker is not None and node == seeker.left:
            node = seeker
            seeker = seeker.left
        return seeker


def test():
    array = [3, 1, 5, 2, 4, 6]
    bst = BinarySearchTree(array)
    print(bst)
    bst.insert(7)
    print(bst)
    seeker = bst.search(5)
    print(seeker)
    print(bst.min())
    print(bst.max())
    bst.in_order_traversal(bst.search(3))
    print(bst.min_subtree(bst.search(5)))
    print(bst.successor(bst.search(2)))
    print(bst.predecessor(bst.search(5)))
    bst.delete(5)
    print(bst)


if __name__ == '__main__':
    test()
