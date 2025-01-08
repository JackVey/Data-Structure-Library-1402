import math, random

class Node:
    def __init__(self, ts, value) -> None:
        self.ts = ts
        self.value = value
        self.priority = math.floor(random.random() * 100000)
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.ts < x.ts:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.ts < y.ts:
            y.left = node
        else:
            y.right = node
        
    def search(self, key):
        x = self.root
        while x is not None and key != x.ts:
            if key < x.ts:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_print(self, root):
        if root is not None:
            self.inorder_print(root.left)
            print(root.ts, end=" ")
            self.inorder_print(root.right)
    
    def left_rotate(self, x):
        # TODO
        pass

    def right_rotate(self, y):
        # TODO
        pass
    
    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x.ts

    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x.ts
    
    def successor(self, x):
        # TODO
        pass

    def predecessor(self, x):
        # TODO
        pass

    def fixup_insert(self, z):
        # TODO
        pass

    def search_or_sum(self, ts1, ts2):
        # TODO
        pass

    def sum_values_between(self, node, ts1, ts2):
        # TODO
        pass
    
def main():
    # TODO
    pass    

if __name__ == '__main__':
    main()