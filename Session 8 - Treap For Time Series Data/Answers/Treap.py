import random
import time


class record:
    def __init__(self, name, f):
        self.name = name
        self.f = f


class Node:
    def __init__(self, item):
        self.key = item
        self.priority = 0
        self.left = None
        self.right = None
        self.parent = None


class Treap:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)

    def insert(self, z):
        z.priority = random.randint(1, 10000000)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key.name < x.key.name:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key.name < y.key.name:
            y.left = z
        else:
            y.right = z
        self.fix_up(z)

    def search(self, k):
        x = self.root
        while x is not None and k != x.key.name:
            if k < x.key.name:
                x = x.left
            else:
                x = x.right
        return x

    def right_rotate(self, y):
        x = y.left
        if y.parent is not None:
            if y.parent.right == y:
                y.parent.right = x
            else:
                y.parent.left = x
        x.parent = y.parent
        y.parent = x
        T2 = x.right
        x.right = y
        y.left = T2
        if T2 is not None:
            T2.parent = y

    def left_rotate(self, x):
        y = x.right

        if x.parent is not None:
            if x.parent.right == x:
                x.parent.right = y
            else:
                x.parent.left = y

        y.parent = x.parent
        x.parent = y
        T2 = y.left
        y.left = x
        x.right = T2
        if T2 is not None:
            T2.parent = x

    def fix_up(self, node):
        if node.parent is None:
            self.root = node
            return
        if node.priority <= node.parent.priority:
            return
        if node.parent.left == node:
            self.right_rotate(node.parent)
            self.fix_up(node)
        else:
            self.left_rotate(node.parent)
            self.fix_up(node)

    def minimum(self, x):
        while x.left:
            x = x.left
        return x

    def maximum(self, x):
        while x.right:
            x = x.right
        return x

    def predecessor(self, x):
        if x.left:
            return self.maximum(x.left)
        else:
            while x.parent and x == x.parent.left:
                x = x.parent
            return x.parent

    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        else:
            while x.parent and x == x.parent.right:
                x = x.parent
            return x.parent

    # def findMaxForN(self, root, N):
    #
    #     if root == None:
    #         return -1
    #     if root.key.name == N:
    #         return root.key.f
    #
    #     elif root.key.name < N:
    #         k = self.findMaxForN(root.right, N)
    #         if k == -1:
    #             return root.key.f
    #         else:
    #             return k
    #
    #
    #     elif root.key.name > N:
    #         return self.findMaxForN(root.left, N)

    def inorder_print(self, root):
        if root is not None:
            self.inorder_print(root.left)
            print(root.key.name, end=" ")
            self.inorder_print(root.right)

    def inorder_print_priority(self, root):
        if root is not None:
            self.inorder_print_priority(root.left)
            print(root.priority, end=" ")
            self.inorder_print_priority(root.right)

if __name__ == '__main__':
    DB = Treap()
    DB2 = Treap()
    try:
        with open('db.txt', 'r') as input_file:
            start = time.time()
            for line in input_file:
                string, num = line.split()
                rec = record(string, int(num))
                DB.insert(Node(rec))
            end = time.time()
            print(f"Time to insert to the list for db: {end - start}")
    except FileNotFoundError:
        print("Failed to open the file.")

    try:
        with open('db2.txt', 'r') as input_file:
            start = time.time()
            for line in input_file:
                string, num = line.split()
                rec = record(string, int(num))
                DB2.insert(Node(rec))
            end = time.time()
            print(f"Time to insert to the list for db2: {end - start}")
    except FileNotFoundError:
        print("Failed to open the file.")

    try:
        with open('query1.txt', 'r') as query_file:
            start = time.time()
            for line in query_file:
                # string, num = line.split()
                string = line
                DB.search(string)
            end = time.time()
            print(f"Time to search string the list: {end - start}")
    except FileNotFoundError:
        print("Failed to open the file.")
