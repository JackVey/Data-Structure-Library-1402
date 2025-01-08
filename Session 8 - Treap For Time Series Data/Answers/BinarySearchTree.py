import time


class record:
    def __init__(self,name,number):
        self.name = name
        self.number = number
class Node:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, z):
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

    def search(self, k):
        x = self.root
        while x is not None and k != x.key.name:
            if k < x.key.name:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_print(self, root):
        if root is not None:
            self.inorder_print(root.left)
            print(root.key, end=" ")
            self.inorder_print(root.right)

if __name__ == '__main__':
    DB = BinarySearchTree()
    DB2 = BinarySearchTree()
    try:
        with open('db.txt', 'r') as input_file:
            start = time.time()
            for line in input_file:
                string, num = line.split()
                rec = record(string, num)
                DB.insert(Node(rec))
            end = time.time()
            print(f"Time to insert to the list for db1: {end - start}")
    except FileNotFoundError:
        print("Failed to open the file.")

    # try:
    #     with open('db2.txt', 'r') as input_file:
    #         start = time.time()
    #         for line in input_file:
    #             string, num = line.split()
    #             rec = record(string, int(num))
    #             DB2.insert(Node(rec))
    #         end = time.time()
    #         print(f"Time to insert to the list for db2: {end - start}")
    # except FileNotFoundError:
    #     print("Failed to open the file.")

    try:
        with open('query1.txt', 'r') as query_file:
            start = time.time()
            for line in query_file:
                string = line
                DB.search(string)
            end = time.time()
            print(f"Time to search string the list: {end - start}")
    except FileNotFoundError:
        print("Failed to open the file.")



    # try:
    #     with open('query2.txt', 'r') as query_file:
    #         start = time.time()
    #         for line in query_file:
    #             string = line
    #             DB.search(string)
    #         end = time.time()
    #         print(f"Time to search not in the db numbers in the list: {end - start}s")
    # except FileNotFoundError:
    #     print("Failed to open the file.")
